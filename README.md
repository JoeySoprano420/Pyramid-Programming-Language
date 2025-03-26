# Pyramid-Programming-Language-Overview:**

**Pyramid** is designed for:
- **Maximum Execution Speed**: High-performance execution for real-time systems.
- **Security Hardness**: Strong security features embedded at the language level.
- **Low-Level Processing**: Supports near-metal operations, ideal for systems programming or embedded systems.
- **AOT (Ahead-Of-Time) Compilation**: Default method of compilation, where code is compiled before execution for optimized performance.
- **JIT (Just-In-Time) Compilation**: Used only for complex edge cases, where real-time conditions require dynamic behavior.

---

### **Key Features of Pyramid**:

#### 1. **Whitespace Ignored**:
   - Reduces unnecessary spaces for tight and optimized code.
   - Easier to write compact code without worrying about formatting.

#### 2. **Explicit Type Declaration**:
   - All variables, functions, and structures must declare their types explicitly.
   - Ensures type safety and reduces errors.

#### 3. **Inline Scripts**:
   - Allows insertion of inline code, which is executed at runtime via JIT.
   - Useful for dynamic event handling or runtime logic that isn’t predetermined.

#### 4. **Macros as Comments**:
   - Comments are treated as macros.
   - Single-line comments use `#`, and multi-line comments use `|| ... ||`.
   - This structure helps the compiler ignore comments while processing the code.

#### 5. **Punctuation Inference**:
   - Punctuation like semicolons, braces, and parentheses is inferred based on context.
   - Optional explicit punctuation for clarity.

#### 6. **AOT (Ahead-Of-Time) Compilation**:
   - Default compilation method ensures all code is precompiled before execution.
   - Provides the best possible performance with minimal overhead.
   - JIT is used only for advanced scenarios, such as complex conditionals.

#### 7. **JIT (Just-In-Time) Compilation**:
   - Triggered for advanced conditional checks or extended boolean logic.
   - Provides flexibility for runtime optimizations when necessary.

---

### **Data Types**:

1. **Primitive Types**:
   - `int`: Integer type.
   - `float`: Floating-point type.
   - `char`: Character type.
   - `bool`: Boolean type.

2. **Complex Types**:
   - `array`: Array type.
   - `map`: Key-value mapping type.
   - `function`: Function type.
   - `object`: Custom object/structure type.

3. **Special Types**:
   - `hex`: Direct hexadecimal values for low-level operations.
   - `asm`: Inline assembly code for near-metal programming.

---

### **Core Language Features**:

1. **Macros as Comments**: 
   - **Single-line comments**: `# This is a comment`.
   - **Multi-line comments**: `|| ... ||`.

2. **Explicit Type Declaration**: 
   - Ensures clarity by requiring all variables, functions, and return types to be explicitly declared. Example: 
     ```pyramid
     def calcInterest(principal:int, rate:float, time:int) -> float {
       let interest:float = principal * rate * time / 100
       return interest
     }
     ```

3. **Inline Scripts for Event Handling**:
   - Allows users to write inline event-driven scripts. For example:
     ```pyramid
     eventEmitter.on('data', (data) => {
       if (data == 'critical') {
         print("Critical Data Received")
       } else {
         print("Normal Data")
       }
     })
     ```

4. **Inline Assembly (asm)**:
   - Supports low-level processing via assembly code embedded within functions. Example:
     ```pyramid
     def lowLevelOperation() {
       asm "MOV R1, 0x100" # Move value into register
       asm "ADD R1, 0x10"  # Add value to register
       asm "MOV 0x200, R1" # Store result in memory
     }
     ```

5. **AOT-based Functions**:
   - Ensures pre-compilation for faster execution. Example:
     ```pyramid
     def transferFunds(sender:object, receiver:object, amount:int) {
       if sender.balance >= amount {
         sender.balance -= amount
         receiver.balance += amount
         logTransaction(sender, receiver, amount)
       } else {
         throw Error("Insufficient Funds")
       }
     }
     ```

6. **Main Execution Entry Point**:
   - Example of the main function that demonstrates a typical Pyramid program:
     ```pyramid
     def main() {
       let principal:int = 1000
       let rate:float = 5.0
       let time:int = 2
       let interest:float = calcInterest(principal, rate, time)
       print("Calculated Interest: ", interest)

       let sender:object = { balance: 2000 }
       let receiver:object = { balance: 500 }
       transferFunds(sender, receiver, 300)
       print("Sender Balance: ", sender.balance)
       print("Receiver Balance: ", receiver.balance)
     }
     ```

---

### **Summary of Key Features**:
- **Inline Scripts** for real-time execution and event handling.
- **Macros as Comments** for better documentation and compiler clarity.
- **Whitespace Ignored** for compact code.
- **Explicit Typing** for safety and clarity.
- **Assembly Inlining** (`asm`) for optimized, low-level operations.
- **AOT Compilation** for optimal performance by default, with **JIT** for edge cases.
- **Advanced Boolean Logic** for handling complex conditions.
- **Contextual Punctuation Inference** for user-friendly syntax.

---

### **Potential Use Cases**:
- **Systems Programming**: Ideal for building high-performance system software or embedded systems.
- **Real-Time Applications**: Supports dynamic, high-performance, real-time decision-making processes.
- **Low-Level Hardware Interaction**: The ability to embed assembly directly within the language makes Pyramid perfect for near-metal operations.

The **Pyramid** language design focuses on optimizing every aspect of performance and security, making it a great choice for applications requiring both speed and precision at a low level of abstraction.

