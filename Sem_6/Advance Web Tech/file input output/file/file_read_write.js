const fs = require('fs');

fs.readFile("input.txt", 'utf-8', (err, data) => {
    if (err) {
        console.error("Error reading file: ", err);
        return;
    }
    console.log("File content: ", data);

    const nd = `${data}\n This is the appended text: `;
    fs.writeFile("output.txt", nd, (err) => {
        if (err) {
            console.error("Error writing file: ", err);
        } else {
            console.log("File has been written to output.txt");
        }
    });
});

