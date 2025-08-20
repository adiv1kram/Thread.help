import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown'; // Import the markdown component
import './App.css';
import Starfield from './Starfield';

function App() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [result, setResult] = useState('');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedFile(file);
            setResult('');
            setError('');
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!selectedFile) {
            setError('Please select a Java thread dump file.');
            return;
        }

        setIsLoading(true);
        setError('');
        setResult('');

        const formData = new FormData();
        formData.append('dumpfile', selectedFile);

        try {
            const response = await fetch('http://127.0.0.1:5000/analyze', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || `Server error: ${response.status}`);
            }
            
            //To extract the 'analysis' field from the JSON response
            setResult(data.analysis);

        } catch (err) {
            setError(`Connection failed: ${err.message}. Is the backend server running with a valid API key?`);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <Starfield />
            <div className="app-container">
                <header className="app-header">
                    <h1>Thread.help</h1>
                    <p>Advanced Analysis for Java Thread Dumps</p>
                </header>

                <main className="app-main">
                    <div className="upload-section">
                        <form onSubmit={handleSubmit}>
                            <label htmlFor="dump-file-input" className="file-label">
                                Click to select a thread dump file (.txt)
                            </label>
                            <input
                                type="file"
                                id="dump-file-input"
                                accept=".txt"
                                onChange={handleFileChange}
                                required
                            />
                            {selectedFile && <span className="file-name">Selected: {selectedFile.name}</span>}
                            <button type="submit" disabled={isLoading}>
                                {isLoading ? 'Analyzing...' : 'Analyze Thread Dump'}
                            </button>
                        </form>
                    </div>

                    <div className="solution-pane">
                        {isLoading && <div className="loader"></div>}
                        
                        {!isLoading && !error && !result && (
                            <div className="placeholder">
                                Your analysis and solutions will appear here.
                            </div>
                        )}
                        
                        {error && (
                            <div className="result-content error">
                                <h2>Error</h2>
                                <pre><code>{error}</code></pre>
                            </div>
                        )}

                        {result && (
                             <div className="result-content">
                                <h2>Analysis Result</h2>
                                {/* Use ReactMarkdown to render the result */}
                                <ReactMarkdown>{result}</ReactMarkdown>
                            </div>
                        )}
                    </div>
                </main>
            </div>
        </>
    );
}

export default App;
