import React, { useState } from 'react';
import './App.css';
import Starfield from './Starfield'; // Import the Starfield component

function App() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [result, setResult] = useState('');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedFile(file);
            setResult(''); // Clear previous results
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
            await new Promise(resolve => setTimeout(resolve, 1500)); 
            
            const mockResponse = {
                summary: "The application is experiencing severe thread contention.",
                diagnosis: [
                    {
                        problem: "Deadlock Detected",
                        details: "Threads 'Thread-A' and 'Thread-B' are in a deadlock.",
                        evidence: "Thread 'Thread-A' waiting for lock <0x001> held by 'Thread-B', while 'Thread-B' is waiting for lock <0x002> held by 'Thread-A'."
                    }
                ],
                recommendations: [
                    "Review synchronization blocks for 'com.example.ResourceA' and 'com.example.ResourceB' to ensure consistent lock acquisition order.",
                    "Consider using java.util.concurrent locks with timeouts to prevent indefinite blocking."
                ]
            };
            
            setResult(JSON.stringify(mockResponse, null, 2));

        } catch (err) {
            setError('Failed to analyze the file. Please try again.');
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
                                <pre><code>{result}</code></pre>
                            </div>
                        )}
                    </div>
                </main>
            </div>
        </>
    );
}

export default App;
