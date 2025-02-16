const fs = require('fs');

// Function to read the content of the input file
fs.readFile("input.txt", 'utf-8', (err, data) => {
    if (err) {
        console.error("Failed to read the input file. Error:", err);
        return;
    }

    console.log("Original content of input.txt:", data);

    // Add a timestamp and custom appended text
    const timestamp = new Date().toISOString();
    const additionalText = `\nThis is the appended text:\nTimestamp: ${timestamp}`;
    const updatedContent = `${data}${additionalText}`;

    // Write the modified content to output.txt
    fs.writeFile("output.txt", updatedContent, (err) => {
        if (err) {
            console.error("Failed to write to output file. Error:", err);
        } else {
            console.log("Updated content has been written to output.txt successfully.");

            // Confirm the content by reading output.txt
            fs.readFile("output.txt", 'utf-8', (err, finalData) => {
                if (err) {
                    console.error("Failed to read the output file. Error:", err);
                } else {
                    console.log("Content of output.txt:", finalData);
                }
            });
        }
    });
});

