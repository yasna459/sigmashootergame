---
layout: post
title: Crypto Mining Simulator
type: issues
permalink: /crypto/mining
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-zoom/2.0.1/chartjs-plugin-zoom.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<style>
       .notification { /* This entire style, ".notification", is what makes the notification pops out from the top right! */
       position: fixed;
       top: 20px;
       right: 20px;
       background-color: #333;
       color: white;
       padding: 10px;
       border-radius: 5px;
       z-index: 1000; // Ensure it appears above other elements
   }
   .shadow-red-glow {
    box-shadow: 0 4px 15px -3px rgba(239, 68, 68, 0.3);
    }
    .shadow-green-glow {
        box-shadow: 0 4px 15px -3px rgba(16, 185, 129, 0.3);
    }
   /* GPU Inventory Styles */
   .dashboard-card {
       @apply bg-gray-800 rounded-lg p-6 shadow-lg border border-gray-700;
       transition: transform 0.2s, box-shadow 0.2s;
   }
   .dashboard-card:hover {
       transform: translateY(-2px);
       box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
   }
   .dashboard-card h2 {
       @apply text-xl font-bold mb-4 text-blue-400;
       border-bottom: 2px solid rgba(59, 130, 246, 0.2);
       padding-bottom: 0.5rem;
   }
   .stat-label {
       @apply text-gray-400 text-sm font-medium mb-1;
   }
   .stat-value {
       @apply text-2xl font-bold;
       text-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
   }
   #gpu-inventory {
       @apply mt-4;
       min-height: 200px; /* Ensure minimum height even when empty */
   }
   .gpu-card {
       @apply bg-gray-800 rounded-lg p-4 shadow-lg mb-4;
       border: 1px solid rgba(255, 255, 255, 0.1);
   }
    /* Navigation Bar */
    .navbar-logo {
        font-size: 1.5rem;
        font-weight: bold;
    }
    .navbar-links {
        display: flex;
        gap: 15px;
    }
    .navbar-links a:hover {
        background-color: #575757;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #001f3f; /* Dark blue background */
        color: #fff;
    }
    .navbar .logo {
        font-size: 24px;
        font-weight: bold;
        letter-spacing: 2px;
    }
    .navbar .nav-buttons {
        display: flex;
        gap: 20px;
    }
    .navbar .nav-buttons a {
        color: #fff;
        text-decoration: none;
        font-size: 16px;
        padding: 8px 16px;
        border-radius: 4px;
        transition: background-color 0.3s;
    }
    .navbar .nav-buttons a:hover {
        background-color: #ff8c00; /* Orange hover effect */
    }
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
}
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #001f3f;
    color: #fff;
}
.navbar .logo {
    font-size: 24px;
    font-weight: bold;
    letter-spacing: 2px;
}
.navbar .nav-buttons {
    display: flex;
    gap: 20px;
}
.navbar .nav-buttons a {
    color: #fff;
    text-decoration: none;
    font-size: 16px;
    padding: 8px 16px;
    border-radius: 4px;
    transition: background-color 0.3s;
}
.navbar .nav-buttons a:hover {
    background-color: #ff8c00;
}
.dashboard {
    padding: 20px;
    display: flex;
    justify-content: flex-start;
    gap: 40px;
}
.dashboard-content {
    width: 70%;
}
.sidebar {
    width: 25%;
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.stock-table, .your-stocks {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.your-stocks, .stock-table {
    height: full;
}
.stock-table table, .your-stocks table {
    width: 100%;
    border-collapse: collapse;
}
.stock-table table, th, td, .your-stocks table, th, td {
    border: none;
}
.stock-table th, td, .your-stocks th, td {
    padding: 10px;
    text-align: left;
}
.stock-table th, .your-stocks th {
    background-color: #f2f2f2;
}
.welcome {
    font-size: 24px;
    font-weight: bold;
}
.summary-cards {
    display: flex;
    justify-content: space-between;
    margin: 20px 0;
}
.card {
    padding: 0px;
    margin: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    flex: 1;
    text-align: center;
    color: #fff;
    padding-bottom: -40px;
}
.card-orange {
    background-color: #FF8C00;
}
.card-purple {
    background-color: #6A0DAD;
}
.card-darkblue {
    background-color: #001f3f;
}
.card h2 {
    font-size: 20px;
}
.card p {
    font-size: 36px;
    font-weight: bold;
}
.chart-container {
    @apply bg-gray-800 rounded-lg p-6 border border-gray-700;
    height: 300px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.chart {
    height: 100%;
    width: 100%;
    background-color: #fff;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: #999;
    flex: 1;
}
.search-container {
    margin-bottom: 20px;
    display: flex;
}
.search-container input[type="text"] {
    width: 100%;
    padding: 12px;
    border: none;
    border-radius: 4px;
    outline: none;
    font-size: 16px;
}
.search-button {
    background-color: #ff8c00;
    color: #fff;
    border: none;
    border-radius: 0 4px 4px 0;
    padding: 12px 20px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}
.search-button:hover {
    background-color: #e07b00;
}
</style>
<body class="bg-gray-900 text-white min-h-screen p-6">
    <div class="text-center mb-4 text-yellow-400">
        *** note: If the stats number are not showing, try to stop the mining and start again... <br>
        *** note: If it says "Error loading mining state. Please try again.", please check if you are logged in or no...
    </div>
    <!-- Navigation Bar -->
    <div class="navbar">
        <div class="navbar-logo">Crypto Mining</div>
        <div class="navbar-links">
            <a href="/portfolio_2025/crypto/portfolio">Portfolio</a>
            <a href="/portfolio_2025/crypto/mining">Mining</a>
            <a href="/portfolio_2025/stocks/home">Stocks</a>
        </div>
    </div>
    <div class="container mx-auto">
        <!-- Core Stats Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <!-- Wallet -->
            <div class="dashboard-card">
                <h2>Wallet</h2>
                <div class="grid gap-2">
                    <div>
                        <div class="stat-label">BTC Balance</div>
                        <div class="stat-value" id="btc-balance">0.00000000</div>
                    </div>
                    <div>
                        <div class="stat-label">Pending BTC</div>
                        <div class="stat-value text-yellow-400" id="pending-balance">0.00000000</div>
                    </div>
                    <div>
                        <div class="stat-label">USD Value</div>
                        <div class="stat-value" id="usd-value">$0.00</div>
                    </div>
                    <div>
                        <div class="stat-label" id="pool-info">Min. Payout: 0.001 BTC</div>
                    </div>
                </div>
            </div>
            <!-- Mining Stats -->
            <div class="dashboard-card">
                <h2>Mining Stats</h2>
                <div class="grid gap-2">
                    <div>
                        <div class="stat-label">Hashrate</div>
                        <div class="stat-value" id="hashrate">0 MH/s</div>
                    </div>
                    <div>
                        <div class="stat-label">Shares</div>
                        <div class="stat-value" id="shares">0</div>
                    </div>
                </div>
            </div>
            <!-- Hardware -->
            <div class="dashboard-card">
                <h2>Hardware</h2>
                <div class="grid gap-2">
                    <div>
                        <div class="stat-label">Current GPU</div>
                        <div class="stat-value text-blue-400" id="current-gpu">No GPU</div>
                    </div>
                    <div>
                        <div class="stat-label">GPU Temperature</div>
                        <div class="stat-value" id="gpu-temp">0°C</div>
                    </div>
                    <div>
                        <div class="stat-label">Power Draw</div>
                        <div class="stat-value" id="power-draw">0W</div>
                    </div>
                </div>
            </div>
            <!-- Profitability -->
            <div class="dashboard-card">
                <h2>Profitability</h2>
                <div class="grid gap-2">
                    <div>
                        <div class="stat-label">24h Revenue</div>
                        <div class="stat-value" id="daily-revenue">$0.00</div>
                    </div>
                    <div>
                        <div class="stat-label">Power Cost</div>
                        <div class="stat-value text-red-400" id="power-cost">$0.00</div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Mining Controls -->
        <div class="flex justify-center mt-8 mb-8">
            <div class="flex justify-between items-center">
                <button id="start-mining" class="mining-button">
                    Start Mining
                </button>
            </div>
        </div>
        <!-- Performance Charts -->
        <div class="flex flex-col gap-4 mt-4">
            <div class="text-sm text-gray-400 text-center">
                Drag to pan horizontally • Use mouse wheel to zoom • Double click to reset
            </div>
            <div class="chart-container">
                <canvas id="hashrate-chart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="profit-chart"></canvas>
            </div>
        </div>
        <!-- GPU Inventory -->
        <div class="dashboard-card mt-4 bg-gray-900 p-6 rounded-lg">
            <div class="flex justify-between items-center mb-4">
                <h2 class="text-xl font-bold">My GPU Inventory</h2>
                <button id="gpu-shop" 
                        class="bg-indigo-600 hover:bg-indigo-700 px-6 py-3 rounded-lg 
                               font-medium transition-colors duration-200 flex items-center gap-2">
                    <span>🛒</span>
                    GPU Shop
                </button>
            </div>
            <div id="gpu-inventory" class="min-h-[400px]">
            </div>
        </div>
    </div>
    <!-- GPU Shop Modal -->
    <div id="gpu-shop-modal" class="fixed inset-0 bg-black bg-opacity-50 hidden z-50">
        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 
                    bg-gray-800 rounded-lg p-6 w-11/12 max-w-4xl max-h-[80vh] overflow-hidden">
            <div class="flex justify-between items-center mb-4">
                <h2 class="text-2xl font-bold">GPU Shop</h2>
                <button id="close-shop" class="text-gray-400 hover:text-white text-3xl">&times;</button>
            </div>
            <div class="overflow-y-auto pr-2" style="max-height: calc(80vh - 100px);">
                <div id="gpu-list" class="grid gap-4">
                    <!-- GPUs will be inserted here -->
                </div>
            </div>
        </div>
    </div>
    <script type="module">
        import { login, pythonURI, javaURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js'; //imports config.js
        let hashrateChart, profitChart;
        let updateInterval;
        // Initialize charts and setup
        document.addEventListener('DOMContentLoaded', async () => {
            try {
                initializeCharts();
                setupEventListeners();
                await initializeMiningState();
                await loadGPUs();
            } catch (error) {
                console.error('Error during initialization:', error);
            }
        });
        function initializeCharts() {
            // Hashrate Chart
            const hashrateCtx = document.getElementById('hashrate-chart').getContext('2d');
            hashrateChart = new Chart(hashrateCtx, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        label: 'Hashrate (MH/s)',
                        data: [],
                        borderColor: '#3B82F6',
                        backgroundColor: 'rgba(59, 130, 246, 0.2)',
                        borderWidth: 3,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        zoom: {
                            zoom: {
                                wheel: { enabled: true },
                                pinch: { enabled: true },
                                mode: 'x'
                            },
                            pan: { enabled: true }
                        }
                    }
                }
            });
            // Profit Chart
            const profitCtx = document.getElementById('profit-chart').getContext('2d');
            profitChart = new Chart(profitCtx, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        label: 'Profit (USD)',
                        data: [],
                        borderColor: '#BE0102',
                        backgroundColor: 'rgba(190, 1, 2, 0.2)',
                        borderWidth: 3,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        zoom: {
                            zoom: {
                                wheel: { enabled: true },
                                pinch: { enabled: true },
                                mode: 'x'
                            },
                            pan: { enabled: true }
                        }
                    }
                }
            });
        }
        function setupEventListeners() {
            document.getElementById('start-mining').addEventListener('click', toggleMining);
            document.getElementById('gpu-shop').addEventListener('click', openGpuShop);
        }
        async function initializeMiningState() {
            try {
                const options = {
                    ...fetchOptions,
                    method: 'GET',
                    cache: 'no-cache'
                };
                // Fetch initial mining state
                const response = await fetch(`${javaURI}/api/mining/state`, options);
                if (!response.ok) {
                    throw new Error('Failed to fetch mining state');
                }
                const state = await response.json();
                console.log('Initial mining state:', state);
                // Update UI with initial state
                updateDisplay(state);
                updateMiningButton(state.isMining);
                // Start periodic updates if mining is active
                if (state.isMining) {
                    startPeriodicUpdates();
                }
            } catch (error) {
                console.error('Error initializing mining state:', error);
                showNotification('Error loading mining state. Please try again.');
            }
        }
        async function startPeriodicUpdates() {
            if (updateInterval) {
                clearInterval(updateInterval);
            }
            // Update mining stats every minute
            updateInterval = setInterval(async () => {
                await updateMiningStats();
            }, 60000);
            // Add frequent updates for temperature and power
            setInterval(() => {
                const statsElement = document.getElementById('gpu-temp');
                const powerElement = document.getElementById('power-draw');
                if (statsElement && powerElement) {
                    const currentTemp = parseFloat(statsElement.textContent);
                    const currentPower = parseFloat(powerElement.textContent);
                    if (!isNaN(currentTemp) && !isNaN(currentPower)) {
                        const tempVariation = Math.random() * 2 - 1;
                        const powerVariation = Math.random() * 10 - 5;
                        const newTemp = Math.max(30, Math.min(90, currentTemp + tempVariation));
                        const newPower = Math.max(0, currentPower + powerVariation);
                        statsElement.textContent = `${newTemp.toFixed(1)}°C`;
                        powerElement.textContent = `${newPower.toFixed(0)}W`;
                        // Update temperature color
                        if (newTemp >= 80) {
                            statsElement.className = 'stat-value text-red-500';
                        } else if (newTemp >= 70) {
                            statsElement.className = 'stat-value text-yellow-500';
                        } else {
                            statsElement.className = 'stat-value text-green-500';
                        }
                    }
                }
            }, 2000); // Update every 2 seconds
            // 在startPeriodicUpdates中添加
            setInterval(async () => {
                const options = {
                    ...fetchOptions,
                    method: 'GET',
                    cache: 'no-cache'
                };
                try {
                    const response = await fetch(`${javaURI}/api/mining/stats`, options);
                    const stats = await response.json();
                    console.log('实时监控:', {
                        time: new Date().toLocaleTimeString(),
                        pending: stats.pendingBalance,
                        hashrate: stats.hashrate,
                        activeGPUs: stats.activeGPUs?.length || 0
                    });
                } catch (error) {
                    console.error('实时监控错误:', error);
                }
            }, 5000); // 每5秒更新
        }
        // API Calls
        async function loadGPUs() {
            try {
                const options = {
                    ...fetchOptions,
                    method: 'GET',
                    cache: 'no-cache'
                };
                const response = await fetch(`${javaURI}/api/mining/shop`, options);
                const gpus = await response.json();
                console.log('GPUs:', gpus); // Log the GPUs to check the structure
                renderGpuShop(gpus);
            } catch (error) {
                console.error('Error loading GPUs:', error);
            }
        }
        async function toggleMining() {
            try {
                const options = {
                    ...fetchOptions,
                    method: 'POST',
                    cache: 'no-cache'
                };
                const response = await fetch(`${javaURI}/api/mining/toggle`, options);
                const result = await response.json();
                console.log('Mining toggle result:', result);
                updateMiningButton(result.isMining);
                if (result.isMining) {
                    startPeriodicUpdates();
                    showNotification('Mining started successfully');
                } else {
                    stopPeriodicUpdates();
                    showNotification('Mining stopped');
                }
                await updateMiningStats();
            } catch (error) {
                console.error('Error toggling mining:', error);
                showNotification('Error toggling mining state');
            }
        }
        window.toggleGPU = async function(gpuId) {
            try {
                const options = {
                    ...fetchOptions,
                    method: 'POST',
                    cache: 'no-cache'
                };
                const response = await fetch(`${javaURI}/api/mining/gpu/toggle/${gpuId}`, options);
                const result = await response.json();
                if (result.success) {
                    showNotification(result.message);
                    // 局部更新GPU卡片
                    const gpuCard = document.querySelector(`[data-gpu-id="${gpuId}"]`);
                    if (gpuCard) {
                        const button = gpuCard.querySelector('button');
                        button.innerHTML = `
                            <span class="text-lg">${result.isActive ? '⏸️' : '▶️'}</span>
                            ${result.isActive ? 'Deactivate' : 'Activate'}
                        `;
                        button.className = `w-full ${result.isActive ? 'bg-red-500 hover:bg-red-600' : 'bg-green-500 hover:bg-green-600'} 
                            px-6 py-3 rounded-lg font-medium transition-colors duration-200 flex items-center justify-center gap-2`;
                    }
                    // 只更新统计数字，不重新渲染整个列表
                    await updateMiningStats();
                } else {
                    showNotification(result.message || 'Failed to toggle GPU');
                }
            } catch (error) {
                console.error('Error toggling GPU:', error);
                showNotification('Error toggling GPU: ' + error.message);
            }
        }
        window.buyGpu = async function(gpuId) {
            try {
                const options = {
                    ...fetchOptions,
                    method: 'POST',
                    cache: 'no-cache'
                };
                const response = await fetch(`${javaURI}/api/mining/gpu/buy/${gpuId}`, options);
                const result = await response.json();
                if (response.ok) {
                    showNotification(result.message);
                    await updateMiningStats(); // This will update the GPU inventory
                    await loadGPUs(); // This will update the shop
                } else {
                    showNotification(result.message || 'Failed to buy GPU');
                }
            } catch (error) {
                console.error('Error buying GPU:', error);
                showNotification('Error buying GPU: ' + error.message);
            }
        }
        async function switchPool(event) {
            try {
                const options = {
                    ...fetchOptions,
                    method: 'POST',
                    cache: 'no-cache',
                    body: JSON.stringify({ pool: event.target.value })
                };
                const response = await fetch(`${javaURI}/api/mining/pool`, options);
                const result = await response.json();
                if (result.success) {
                    showNotification(`Switched to ${event.target.value}`);
                }
            } catch (error) {
                console.error('Error switching pool:', error);
            }
        }
        async function updateMiningStats() {
            try {
                const options = {
                    ...fetchOptions,
                    method: 'GET',
                    cache: 'no-cache'
                };
                const response = await fetch(`${javaURI}/api/mining/stats`, options);
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const stats = await response.json();
                console.log('完整统计信息:', {
                    pendingBalance: stats.pendingBalance,
                    shares: stats.shares,
                    hashrate: stats.hashrate,
                    activeGPUs: stats.activeGPUs
                });
                if (!stats.gpus) {
                    console.warn('API response missing gpus field', stats);
                    stats.gpus = []; // Set default
                }
                updateDisplay(stats);
                renderGpuInventory(stats);
                updateCharts(stats);
            } catch (error) {
                console.error('Error updating mining stats:', error);
                showNotification('Failed to fetch mining data, check your connection');
            }
        }
        // UI Updates
        function updateDisplay(stats) {
            if (!stats) return;
            // Add small random fluctuations to temperature and power
            const tempVariation = Math.random() * 2 - 1; // Random variation ±1°C
            const powerVariation = Math.random() * 10 - 5; // Random variation ±5W
            // Get base values
            const baseTemp = parseFloat(stats.averageTemperature) || 0;
            const basePower = parseFloat(stats.powerConsumption) || 0;
            // Calculate new values with fluctuations
            const newTemp = Math.max(30, Math.min(90, baseTemp + tempVariation)); // Keep between 30-90°C
            const newPower = Math.max(0, basePower + powerVariation); // Keep above 0W
            // Update display elements
            document.getElementById('btc-balance').textContent = (parseFloat(stats.btcBalance) || 0).toFixed(8);
            document.getElementById('pending-balance').textContent = 
                (parseFloat(stats.pendingBalance) || 0).toFixed(8);
            document.getElementById('hashrate').textContent = `${(parseFloat(stats.hashrate) || 0).toFixed(2)} MH/s`;
            document.getElementById('shares').textContent = stats.shares || 0;
            document.getElementById('gpu-temp').textContent = `${newTemp.toFixed(1)}°C`;
            document.getElementById('power-draw').textContent = `${newPower.toFixed(0)}W`;
            document.getElementById('daily-revenue').textContent = `$${(typeof stats.dailyRevenue === 'number' ? stats.dailyRevenue : 0).toFixed(2)}`;
            document.getElementById('power-cost').textContent = `$${(typeof stats.powerCost === 'number' ? stats.powerCost : 0).toFixed(2)}`;
            // Update current GPU display
            if (stats.gpus && stats.gpus.length > 0) {
                const activeGpu = stats.gpus.find(gpu => gpu.isActive);
                document.getElementById('current-gpu').textContent = activeGpu ? activeGpu.name : 'No Active GPU';
            } else {
                document.getElementById('current-gpu').textContent = 'No GPU';
            }
            // Add color indicators for temperature
            const tempElement = document.getElementById('gpu-temp');
            if (newTemp >= 80) {
                tempElement.className = 'stat-value text-red-500'; // Hot
            } else if (newTemp >= 70) {
                tempElement.className = 'stat-value text-yellow-500'; // Warm
            } else {
                tempElement.className = 'stat-value text-green-500'; // Good
            }
        }
        function renderGpuInventory(stats) {
            console.log('Full stats data:', stats);
            const inventoryElement = document.getElementById('gpu-inventory');
            if (!inventoryElement) {
                console.error('GPU inventory element not found');
                return;
            }
            inventoryElement.innerHTML = '';
            // Safely access gpus array
            const gpus = stats?.gpus || [];
            console.log('Valid GPU data:', gpus);
            if (gpus.length === 0) {
                inventoryElement.innerHTML = `
                    <div class="text-gray-400 text-center p-8 bg-gray-800 rounded-lg w-full">
                        <p class="mb-2">🛒 Inventory empty!</p>
                        <p>Click the button above to visit the GPU shop</p>
                    </div>
                `;
                return;
            }
            // Create card container
            const container = document.createElement('div');
            container.className = 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-4';
            gpus.forEach(gpu => {
                const gpuCard = document.createElement('div');
                gpuCard.className = 'bg-gray-800 rounded-xl p-6 shadow-2xl transform transition-all duration-300 hover:scale-[1.02] border border-gray-700';
                gpuCard.dataset.gpuId = gpu.id;
                // Safely access properties
                const hashrate = gpu.hashrate || 0;
                const power = gpu.power || 0;
                const temp = gpu.temp || 0;
                const isActive = !!gpu.isActive;
                const efficiency = (hashrate / (power || 1)).toFixed(3);
                const dailyRevenue = hashrate * 86400 / 1e12;
                const dailyPowerCost = (power * 24) / 1000 * 0.12;
                const dailyProfit = dailyRevenue - dailyPowerCost;
                gpuCard.innerHTML = `
                    <div class="flex flex-col h-full">
                        <div class="flex-1">
                            <h3 class="text-xl font-bold text-white mb-4">${gpu.name}</h3>
                            <div class="grid grid-cols-2 gap-4 mt-2">
                                <div class="text-sm">
                                    <p class="text-gray-400">Performance</p>
                                    <p class="text-white">⚡ ${hashrate.toFixed(2)} MH/s</p>
                                    <p class="text-white">🔌 ${power.toFixed(0)}W</p>
                                    <p class="text-white">🌡️ ${temp.toFixed(1)}°C</p>
                                    <p class="text-white">📊 ${efficiency} MH/W</p>
                                </div>
                                <div class="text-sm">
                                    <p class="text-gray-400">Daily Estimates</p>
                                    <p class="text-green-400">💰 $${dailyRevenue.toFixed(2)}</p>
                                    <p class="text-red-400">💡 -$${dailyPowerCost.toFixed(2)}</p>
                                    <p class="text-blue-400">📈 $${dailyProfit.toFixed(2)}</p>
                                </div>
                            </div>
                        </div>
                        <div class="mt-6 border-t border-gray-700 pt-4">
                            <button onclick="toggleGPU(${gpu.id})" 
                                    class="w-full flex items-center justify-center gap-2 px-6 py-3 rounded-lg font-medium transition-all duration-200 
                                         ${isActive ? 
                                             'bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 shadow-red-glow' : 
                                             'bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 shadow-green-glow'}
                                         transform hover:scale-[1.02] active:scale-95 group">
                                <span class="opacity-90 group-hover:opacity-100 transition-opacity">
                                    ${isActive ? '⏸️' : '▶️'}
                                </span>
                                <span class="text-shadow">${isActive ? 'Deactivate' : 'Activate'}</span>
                            </button>
                        </div>
                    </div>
                `;
                container.appendChild(gpuCard);
            });
            inventoryElement.appendChild(container);
        }
        function updateCharts(stats) {
            if (!stats) {
                console.warn('updateCharts called without stats');
                return;
            }
            console.log('Updating charts with:', {
                hashrate: stats.hashrate,
                dailyRevenue: stats.dailyRevenue,
                powerCost: stats.powerCost
            });
            const now = new Date().toLocaleTimeString();
            // Update hashrate chart
            if (hashrateChart) {
                const numericHashrate = parseFloat(stats.hashrate) || 0;
                console.log('Adding hashrate data point:', numericHashrate);
                hashrateChart.data.labels.push(now);
                hashrateChart.data.datasets[0].data.push(numericHashrate);
                if (hashrateChart.data.labels.length > 50) {
                    hashrateChart.data.labels.shift();
                    hashrateChart.data.datasets[0].data.shift();
                }
                hashrateChart.update('none');
                console.log('Hashrate chart updated');
            }
            // Update profit chart
            if (profitChart) {
                const dailyRevenue = typeof stats.dailyRevenue === 'number' ? stats.dailyRevenue : 0;
                const powerCost = typeof stats.powerCost === 'number' ? stats.powerCost : 0;
                const profit = dailyRevenue - powerCost;
                console.log('Calculated profit:', { dailyRevenue, powerCost, profit });
                profitChart.data.labels.push(now);
                profitChart.data.datasets[0].data.push(profit);
                if (profitChart.data.labels.length > 50) {
                    profitChart.data.labels.shift();
                    profitChart.data.datasets[0].data.shift();
                }
                profitChart.update('none');
                console.log('Profit chart updated');
            }
        }
        function updateMiningButton(isActive) {
            const button = document.getElementById('start-mining');
            if (isActive) {
                button.textContent = 'Stop Mining';
                button.className = 'mining-button active';
            } else {
                button.textContent = 'Start Mining';
                button.className = 'mining-button';
            }
        }
        function renderGpuShop(gpus) {
            const gpuListElement = document.getElementById('gpu-list');
            gpuListElement.innerHTML = '';
            // Group GPUs by category
            const categories = {
                'Free Starter GPU': gpus.filter(gpu => gpu.price === 0),
                'Budget GPUs ($50-500)': gpus.filter(gpu => gpu.price > 0 && gpu.price <= 500),
                'Mid-Range GPUs ($500-1500)': gpus.filter(gpu => gpu.price > 500 && gpu.price <= 1500),
                'High-End GPUs ($1500-3000)': gpus.filter(gpu => gpu.price > 1500 && gpu.price <= 3000),
                'Premium GPUs ($3000+)': gpus.filter(gpu => gpu.price > 3000)
            };
            Object.entries(categories).forEach(([category, categoryGpus]) => {
                if (categoryGpus.length === 0) return;
                const categoryHeader = document.createElement('div');
                categoryHeader.className = `text-xl font-bold mb-4 mt-6 ${getCategoryColor(category)}`;
                categoryHeader.textContent = category;
                gpuListElement.appendChild(categoryHeader);
                categoryGpus.forEach(gpu => {
                    const gpuCard = createGpuCard(gpu, category);
                    gpuListElement.appendChild(gpuCard);
                });
            });
        }
        function createGpuCard(gpu, category) {
            const card = document.createElement('div');
            card.className = `gpu-card mb-4 ${getCategoryClass(category)}`;
            // Calculate daily estimates
            const dailyRevenue = (gpu.hashRate || 0) * 86400 / (1e12); // Ensure hashRate is defined
            const dailyPowerCost = (gpu.powerConsumption || 0) * 24 / 1000 * 0.12; // Ensure powerConsumption is defined
            const dailyProfit = dailyRevenue - dailyPowerCost;
            const roi = dailyProfit > 0 ? (gpu.price / dailyProfit) : Infinity; // Avoid division by zero
            card.innerHTML = `
                <div class="flex justify-between items-start">
                    <div class="flex-1">
                        <h3 class="text-lg font-bold ${getCategoryColor(category)}">${gpu.name}</h3>
                        <div class="grid grid-cols-2 gap-4 mt-2">
                            <div class="text-sm">
                                <p class="text-gray-400">Performance</p>
                                <p class="text-white">⚡ ${(gpu.hashRate || 0).toFixed(2)} MH/s</p>
                                <p class="text-white">🔌 ${(gpu.powerConsumption || 0).toFixed(0)}W</p>
                                <p class="text-white">🌡️ ${(gpu.temperature || 0).toFixed(1)}°C</p>
                            </div>
                            <div class="text-sm">
                                <p class="text-gray-400">Daily Estimates</p>
                                <p class="text-green-400">💰 $${dailyRevenue.toFixed(2)}</p>
                                <p class="text-red-400">💡 -$${dailyPowerCost.toFixed(2)}</p>
                                <p class="text-blue-400">📈 $${dailyProfit.toFixed(2)}</p>
                            </div>
                        </div>
                        <div class="mt-2 text-sm">
                            <p class="text-gray-400">Efficiency: ${((gpu.hashRate || 0) / (gpu.powerConsumption || 1)).toFixed(3)} MH/W</p>
                            <p class="text-gray-400">ROI: ${roi.toFixed(1)} days</p>
                        </div>
                    </div>
                    <div class="text-right ml-4">
                        <p class="text-xl font-bold ${getCategoryColor(category)}">
                            ${gpu.price === 0 ? 'FREE' : '$' + gpu.price.toLocaleString()}
                        </p>
                        <button onclick="window.buyGpu(${gpu.id})" 
                                class="bg-gray-800 hover:bg-gray-700 px-4 py-2 rounded mt-2">
                            ${gpu.price === 0 ? 'Get Free' : 'Buy'}
                        </button>
                    </div>
                </div>
            `;
            return card;
        }
        // Utility functions
        function getCategoryColor(category) {
            const colors = {
                'Free Starter GPU': 'text-green-400',
                'Budget GPUs ($50-500)': 'text-blue-400',
                'Mid-Range GPUs ($500-1500)': 'text-purple-400',
                'High-End GPUs ($1500-3000)': 'text-orange-400',
                'Premium GPUs ($3000+)': 'text-red-400'
            };
            return colors[category] || 'text-white';
        }
        function getCategoryClass(category) {
            const classes = {
                'Free Starter GPU': 'starter',
                'Budget GPUs ($50-500)': 'budget',
                'Mid-Range GPUs ($500-1500)': 'mid-range',
                'High-End GPUs ($1500-3000)': 'high-end',
                'Premium GPUs ($3000+)': 'premium'
            };
            return classes[category] || '';
        }
        function openGpuShop() {
            const modal = document.getElementById('gpu-shop-modal');
            modal.classList.remove('hidden');
        }
        // Add close shop functionality
        document.getElementById('close-shop').addEventListener('click', () => {
            const modal = document.getElementById('gpu-shop-modal');
            modal.classList.add('hidden');
        });
        // Close modal when clicking outside
        document.getElementById('gpu-shop-modal').addEventListener('click', (e) => {
            if (e.target.id === 'gpu-shop-modal') {
                e.target.classList.add('hidden');
            }
        });
        function showNotification(message) {
            console.log('Notification:', message);
            const notificationElement = document.createElement('div');
            notificationElement.textContent = message;
            notificationElement.className = 'notification';
            document.body.appendChild(notificationElement);
            setTimeout(() => {
                document.body.removeChild(notificationElement);
            }, 3000);
        }
        function stopPeriodicUpdates() {
            if (updateInterval) {
                clearInterval(updateInterval);
                updateInterval = null;
            }
        }
    </script>
</body>
</html>