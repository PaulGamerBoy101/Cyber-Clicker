let score = 0;
let scoreIncrement = 1;
let autoClickerCount = 0;
let keyboardCount = 0;

document.getElementById('clicker').addEventListener('click', function() {
    addScore(scoreIncrement);
});

function addScore(amount) {
    score += amount;
    updateScoreDisplay();
}

function updateCountsDisplay() {
    document.getElementById('mouse-count').textContent = (scoreIncrement - 1) / 2;
    document.getElementById('auto-clicker-count').textContent = autoClickerCount;
    document.getElementById('keyboard-count').textContent = keyboardCount;
}

function updatePPSDisplay() {
    // Calculate the total points per second
    let totalPPS = (0.5 * autoClickerCount) + (3 * keyboardCount);
    document.getElementById('points-per-second').textContent = totalPPS.toFixed(1); 
}

function updateScoreDisplay() {
    document.getElementById('score').textContent = score;
    updateUpgradesAvailability(); 
    updateCountsDisplay(); 
    updatePPSDisplay(); 
}


function purchaseUpgrade(upgradeType) {
    if (upgradeType === 1 && score >= 100) {
        score -= 100;
        scoreIncrement += 2;
        updateScoreDisplay();
    } else if (upgradeType === 2 && score >= 50) {
        score -= 50;
        autoClickerCount += 1;
        if (autoClickerCount === 1) {
            startAutoClicker();
        }
        updateScoreDisplay();
    } else if (upgradeType === 3 && score >= 350.5) { 
        score -= 350.5;
        keyboardCount += 1; 
        if (keyboardCount === 1) { 
            startKeyboard(); 
        }
        updateScoreDisplay();
    }
}

function startAutoClicker() {
    setInterval(function() {
        addScore(0.5 * autoClickerCount); 
    }, 1000);
}

function startKeyboard() {
    setInterval(function() {
        addScore(3 * keyboardCount); 
    }, 1000);
}

function updateUpgradesAvailability() {
    let mouseUpgrade = document.querySelector('[data-upgrade="mouse"]');
    if (score < 100) {
        mouseUpgrade.style.color = 'grey';
        mouseUpgrade.removeAttribute('onclick');
    } else {
        mouseUpgrade.style.color = 'black';
        mouseUpgrade.setAttribute('onclick', 'purchaseUpgrade(1)');
    }

    let autoClickerUpgrade = document.querySelector('[data-upgrade="auto-clicker"]');
    if (score < 50) {
        autoClickerUpgrade.style.color = 'grey';
        autoClickerUpgrade.removeAttribute('onclick');
    } else {
        autoClickerUpgrade.style.color = 'black';
        autoClickerUpgrade.setAttribute('onclick', 'purchaseUpgrade(2)');
    }
    
    let keyboardUpgrade = document.querySelector('[data-upgrade="keyboard"]');
    if (score < 350.5) {
        keyboardUpgrade.style.color = 'grey';
        keyboardUpgrade.removeAttribute('onclick');
    } else {
        keyboardUpgrade.style.color = 'black';
        keyboardUpgrade.setAttribute('onclick', 'purchaseUpgrade(3)');
    }

    
}

document.getElementById('clicker').addEventListener('click', function(event) {
    addScore(scoreIncrement);
    createMiniChip(event); // Create the mini chip

    // Apply the wobble effect
    this.classList.add('wobble-effect');

    // Remove the wobble-effect class after the animation ends to allow it to be re-applied on next click
    setTimeout(() => {
        this.classList.remove('wobble-effect');
    }, 500); // Match the duration of the animation
});


updateScoreDisplay();