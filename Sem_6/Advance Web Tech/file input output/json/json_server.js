const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;
const JSON_FILE = 'data.json';

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Endpoint to download the JSON file
app.get('/data', (req, res) => {
    // Set headers to trigger a file download
    res.setHeader('Content-Disposition', 'attachment; filename=output.json');
    res.setHeader('Content-Type', 'application/json');

    fs.readFile(JSON_FILE, 'utf-8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            return res.status(500).send('Error reading data.');
        }
        // Send the content of the file as the download
        res.status(200).send(data);
    });
});

// Endpoint to add new data to the JSON file
app.post('/data', (req, res) => {
    const newData = req.body;

    // Read the current content of the JSON file
    fs.readFile(JSON_FILE, 'utf-8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            return res.status(500).send('Error reading data.');
        }

        // Parse the existing data and add the new data
        const jsonData = JSON.parse(data);
        jsonData.push(newData);

        // Write the updated data back to the JSON file
        fs.writeFile(JSON_FILE, JSON.stringify(jsonData, null, 2), (err) => {
            if (err) {
                console.error('Error writing to JSON file:', err);
                return res.status(500).send('Error saving data.');
            }
            res.status(201).send('Data added successfully.');
        });
    });
});

// Endpoint to update specific data in the JSON file by ID
app.put('/data/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const updatedData = req.body;

    fs.readFile(JSON_FILE, 'utf-8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            return res.status(500).send('Error reading data.');
        }

        const jsonData = JSON.parse(data);
        const itemIndex = jsonData.findIndex(item => item.id === id);

        if (itemIndex === -1) {
            return res.status(404).send('Item not found.');
        }

        // Update the specific item
        jsonData[itemIndex] = { ...jsonData[itemIndex], ...updatedData };

        fs.writeFile(JSON_FILE, JSON.stringify(jsonData, null, 2), (err) => {
            if (err) {
                console.error('Error writing to JSON file:', err);
                return res.status(500).send('Error updating data.');
            }
            res.status(200).send('Data updated successfully.');
        });
    });
});

// Endpoint to delete specific data in the JSON file by ID
app.delete('/data/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);

    fs.readFile(JSON_FILE, 'utf-8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            return res.status(500).send('Error reading data.');
        }

        const jsonData = JSON.parse(data);
        const newData = jsonData.filter(item => item.id !== id);

        fs.writeFile(JSON_FILE, JSON.stringify(newData, null, 2), (err) => {
            if (err) {
                console.error('Error writing to JSON file:', err);
                return res.status(500).send('Error deleting data.');
            }
            res.status(200).send('Data deleted successfully.');
        });
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});

