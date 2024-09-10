function showOperations() {
    const dataType = document.getElementById("dataType").value;
    const operationDropdown = document.getElementById("operation");
  
    // Clear previous options
    operationDropdown.innerHTML =
      '<option value="">-- Select Operation --</option>';
  
    // Enable the operation dropdown
    operationDropdown.disabled = false;
  
    // Add specific operations based on selected data type
    if (dataType === "string") {
      operationDropdown.innerHTML +=
        '<option value="concat">Concatenate</option>';
      operationDropdown.innerHTML +=
        '<option value="substring">Substring</option>';
      operationDropdown.innerHTML +=
        '<option value="length">Length</option>';
      operationDropdown.innerHTML +=
        '<option value="toUpperCase">To Uppercase</option>';
      operationDropdown.innerHTML +=
        '<option value="toLowerCase">To Lowercase</option>';
    } else if (dataType === "array") {
      operationDropdown.innerHTML += '<option value="length">Length</option>';
      operationDropdown.innerHTML += '<option value="pop">Pop</option>';
      operationDropdown.innerHTML += '<option value="push">Push</option>';
      operationDropdown.innerHTML += '<option value="slice">Slice()</option>';
      operationDropdown.innerHTML += '<option value="reverse">Reverse()</option>';
    } else if (dataType === "math") {
      operationDropdown.innerHTML += '<option value="add">Add</option>';
      operationDropdown.innerHTML += '<option value="subtract">Subtract</option>';
      operationDropdown.innerHTML += '<option value="multiply">Multiply</option>';
      operationDropdown.innerHTML += '<option value="divide">Divide</option>';
      operationDropdown.innerHTML += '<option value="modulo">Modulo</option>';
    }
  }
  
  function performOperation() {
    const dataType = document.getElementById("dataType").value;
    const input1 = document.getElementById("input1").value;
    const input2 = document.getElementById("input2").value;
    const operation = document.getElementById("operation").value;
    let output = "";
  
    if (dataType === "string") {
      if (operation === "concat") {
        output = input1 + input2;
      } else if (operation === "substring") {
        const start = parseInt(input2);
        output = input1.substring(start);
      } else if (operation === "length") {
        output = input1.length;
      } else if (operation === "toUpperCase") {
        output = input1.toUpperCase()+input2.toUpperCase();
      } else if (operation === "toLowerCase") {
        output = input1.toLowerCase()+input2.toLowerCase();
      }
    } else if (dataType === "array") {
      let array1 = input1.split(",");
      let array2 = input2.split(",");
  
      if (operation === "length") {
        output = array1.length + array2.length;
      } else if (operation === "pop") {
        array2.forEach((element) => {
          const index = array1.indexOf(element);
          if (index !== -1) {
            array1.splice(index, 1);
          }
        });
        output = array1.toString();
      } else if (operation === "push") {
        array1.push(...array2);
        output = array1.toString();
      } else if (operation === "slice") {
        output = array1.filter((element) => array2.includes(element)).toString();
      } else if (operation === "reverse") {
        output = (array1.concat(array2)).sort().reverse().toString();
      }
    } else if (dataType === "math") {
      const num1 = parseFloat(input1);
      const num2 = parseFloat(input2);
      if (operation === "add") {
        output = num1 + num2;
      } else if (operation === "subtract") {
        output = num1 - num2;
      } else if (operation === "multiply") {
        output = num1 * num2;
      } else if (operation === "divide") {
        output = num1 / num2;
      } else if (operation === "modulo") {
        output = num1 % num2;
      }
    }
  
    document.getElementById("output").innerText = `Result: ${output}`;
  }
  