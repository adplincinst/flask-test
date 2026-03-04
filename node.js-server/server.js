const express = require('express');

// 1. Config
const PORT = 5009;
const app = express();

/**
 * 2. Asynchronous Execution Wrapper (Pygeoapi-style)
 * This handles the transition from the route to the logic.
 */
const executeRequest = async (apiFunc, req, res) => {
    try {
        // We await the result of our core logic
        const { content, status } = await apiFunc();
        
        // Log equivalent to Gunicorn access logs
        console.log(`${new Date().toISOString()} | HTTP ${status} | ${req.method} ${req.url}`);
        
        res.status(status).json(content);
    } catch (error) {
        console.error("Execution Error:", error);
        res.status(500).json({ error: "Internal Server Error" });
    }
};

/**
 * 3. Core Async Logic
 * Uses a Promise-based timeout to simulate a 10s I/O task.
 */
const getStatusData = async () => {
    // Non-blocking sleep for 10,000 milliseconds
    await new Promise(resolve => setTimeout(resolve, 10000));

    return {
        content: {
            status: "online",
            mode: "Asynchronous (Non-blocking)",
            slept: "10 seconds",
            timestamp: new Date().toISOString()
        },
        status: 200
    };
};

/**
 * 4. Define Routes
 * The route handler is marked as 'async'
 */
app.get('/status', async (req, res) => {
    await executeRequest(getStatusData, req, res);
});

// 5. Start Server
app.listen(PORT, () => {
    console.log(`Async Node.js server running on http://localhost:${PORT}`);
    console.log(`Try hitting /status multiple times simultaneously!`);
});

