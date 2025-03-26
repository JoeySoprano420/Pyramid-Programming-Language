import re

# Extended Token Patterns for Pyramid Language and Additional Constructs
TOKEN_PATTERNS = {
    'KEYWORD': r'\b(?:def|let|if|else|while|for|in|return|lambda|type|class|interface|try|catch|finally|import|as|from|yield|match|case|break|continue|pass|raise|with|decorator|operator|override|pyramid|ascend|descend|vertex|layer|base|summit)\b',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',
    'NUMBER': r'\d+(\.\d+)?',
    'STRING': r'"([^"\\]|\\.)*"',  # Handles escaped quotes
    'CHAR': r"'[^']'",
    'OPERATOR': r'==|!=|<=|>=|[-+*/%=!&|^~<>]',
    'ASSIGNMENT_OP': r'[:=]',
    'BRACKET': r'[(){}\[\]]',
    'COMMA': r',',
    'DOT': r'\.',
    'COLON': r':',
    'ARROW': r'->',
    'LAMBDA_ARROW': r'->',
    'COMMENT': r'#.*',
    'MULTI_COMMENT': r'\|\|.*?\|\|',
    'WHITESPACE': r'\s+',
    'INDENT': r'^[ \t]+',  # To track pyramid-like indentation
    'DEDENT': r'(?<=\n)\s+',  # Indentation decrease
}

# AST Node Class with Pyramid-Specific Constructs
class ASTNode:
    def __init__(self, type, value=None, children=None, decorators=None, generic_params=None):
        self.type = type
        self.value = value
        self.children = children if children else []
        self.decorators = decorators or []  # Inline decorators
        self.generic_params = generic_params  # For generics (if any)
        self.pyramid_level = 0  # New attribute to track Pyramid structure level

    def __repr__(self):
        return f"ASTNode(type={self.type}, value={self.value}, pyramid_level={self.pyramid_level}, decorators={self.decorators}, generic_params={self.generic_params}, children={self.children})"

# Extended Symbol Table for Type, Scope, and Pyramid Layer Management
class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.pyramid_layers = {}  # New: Tracks variable definitions at each layer of the Pyramid

    def define(self, name, type, layer=0):
        if layer not in self.pyramid_layers:
            self.pyramid_layers[layer] = {}
        self.pyramid_layers[layer][name] = type

    def lookup(self, name, layer=0):
        for l in range(layer, -1, -1):  # Look up the variable from the current to base layers
            if l in self.pyramid_layers and name in self.pyramid_layers[l]:
                return self.pyramid_layers[l][name]
        return self.symbols.get(name, None)

# Lexer Class with Enhanced Tokenization for Pyramid Structures
class Lexer:
    def __init__(self, patterns):
        self.patterns = [(name, re.compile(pattern)) for name, pattern in patterns.items()]

    def tokenize(self, source_code):
        tokens = []
        indent_stack = [0]  # Stack to handle indentation for Pyramid structure

        while source_code:
            matched = False
            for token_type, pattern in self.patterns:
                match = pattern.match(source_code)
                if match:
                    value = match.group(0)

                    # Track Indents and Dedents
                    if token_type == 'INDENT':
                        current_indent = len(value)
                        if current_indent > indent_stack[-1]:
                            tokens.append(('INDENT', value))
                            indent_stack.append(current_indent)
                        elif current_indent < indent_stack[-1]:
                            tokens.append(('DEDENT', value))
                            indent_stack.pop()
                    elif token_type not in ['WHITESPACE', 'COMMENT', 'MULTI_COMMENT']:
                        tokens.append((token_type, value))
                    source_code = source_code[len(value):]
                    matched = True
                    break
            if not matched:
                raise SyntaxError(f"Unexpected token: {source_code[0]}")
        return tokens

# Extended Parser with Support for Pyramid Blocks
class Parser:
    def __init__(self):
        self.tokens = []
        self.current_token_index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        ast_nodes = []
        while self.current_token_index < len(self.tokens):
            node = self.parse_statement()
            if node:
                ast_nodes.append(node)
        return ast_nodes

    def parse_statement(self):
        token_type, token_value = self.tokens[self.current_token_index]
        if token_type == 'KEYWORD':
            if token_value == 'pyramid':
                return self.parse_pyramid_block()
            elif token_value == 'let':
                return self.parse_variable_declaration()
            elif token_value == 'def':
                return self.parse_function()
            elif token_value == 'class':
                return self.parse_class()
            elif token_value == 'interface':
                return self.parse_interface()
            elif token_value == 'try':
                return self.parse_try_except_block()
        raise SyntaxError(f"Unknown statement starting with token: {token_value}")

    def parse_pyramid_block(self):
        self.consume('KEYWORD', 'pyramid')
        self.consume('BRACKET', '{')
        layers = []
        while self.peek()[1] != '}':
            layers.append(self.parse_layer())
        self.consume('BRACKET', '}')
        return ASTNode('PyramidBlock', children=layers)

    def parse_layer(self):
        self.consume('KEYWORD', 'layer')
        layer_name = self.consume('IDENTIFIER')
        self.consume('BRACKET', '{')
        layer_body = self.parse_block()
        self.consume('BRACKET', '}')
        return ASTNode('Layer', value=layer_name, children=[layer_body])

    # Other parsing methods (parse_function, parse_interface, etc.) remain the same
