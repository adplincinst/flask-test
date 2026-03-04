const express = require('express');

const APP = express();
const PORT = 5009;

/**
 * 1. The Blocking Sleep Helper
 * This is a "Busy-Wait" loop. It keeps the CPU 100% occupied 
 * by checking the time constantly until the delay has passed.
 */
const blockingSleep = (ms) => {
    const start = Date.now();
    console.log(`[${new Date().toISOString()}] BLOCKING the Event Loop...`);
    while (Date.now() - start < ms) {
        // Do nothing, just loop and consume CPU cycles
    }
    console.log(`[${new Date().toISOString()}] Event Loop RELEASED.`);
};

/**
 * 2. Execution Wrapper
 */
const executeRequest = (apiFunc, req, res) => {
    console.log(`[${new Date().toISOString()}] Request received: ${req.url}`);
    
    // We do NOT use 'await' because this function is synchronous and blocking
    const { content, status } = apiFunc();
    
    res.status(status).json(content);
};

/**
 * 3. Core Logic
 */
const getStatusData = () => {
    // This will freeze the entire process for 10 seconds
    blockingSleep(10000); 

    return {
        content: {
            message: "I blocked the entire server for 10 seconds.",
            server: "Node.js (Blocking Mode)",
            warning: "No other requests were handled during this time!"
        },
        status: 200
    };
};

/**
 * 4. Route Definition
 */
APP.get('/status', (req, res) => {
    executeRequest(getStatusData, req, res);
});

// 5. Start the server
APP.listen(PORT, () => {
    console.log(`BLOCKING Server listening on http://localhost:${PORT}`);
});

