import React, { useState } from 'react';
import './App.css';

function App() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [result, setResult] = useState('');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
        setResult(''); // Clear previous results on new file selection
        setError('');
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!selectedFile) {
            setError('Please select a file first.');
            return;
        }

        setIsLoading(true);
        setError('');
        setResult('');

        const formData = new FormData();
        formData.append('dumpfile', selectedFile);

        try {
            const response = await fetch('/analyze', { // Assumes backend runs on the same origin
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setResult(JSON.stringify(data, null, 2));

        } catch (err) {
            setError(err.message);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <main className="App">
            <h1>Thread Dump Analyzer</h1>
            <form onSubmit={handleSubmit}>
                <p>Select a thread dump text file (.txt) to analyze.</p>
                <input
                    type="file"
                    id="dump-file-input"
                    accept=".txt"
                    onChange={handleFileChange}
                    required
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Analyzing...' : 'Analyze'}
                </button>
            </form>

            {isLoading && <div className="loader"></div>}

            {error && (
                <div className="results-container">
                    <h2>Error</h2>
                    <pre><code>{error}</code></pre>
                </div>
            )}

            {result && (
                <div className="results-container">
                    <h2>Analysis Results</h2>
                    <pre><code>{result}</code></pre>
                </div>
            )}
        </main>
    );
}

export default App;