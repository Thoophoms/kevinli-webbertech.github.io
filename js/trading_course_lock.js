// Locks Trading Course pages behind a SHA-256 gated code (secret is sha256("stock")).
window.onload = () => {
    injectTradingLockModal();
    checkTradingCookie();
};

const injectTradingLockModal = () => {
    let style = document.querySelector('style');
    if (!style) {
        style = document.createElement('style');
        document.head.appendChild(style);
    }

    style.textContent += `
        .trading-lock-modal {
            display: flex;
            position: fixed;
            z-index: 999;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            justify-content: center;
            align-items: center;
        }
        .trading-lock-modal-content {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        .trading-lock-blurred {
            filter: blur(8px);
            pointer-events: none;
        }
        .trading-lock-hidden {
            display: none;
        }
    `;

    const modalHTML = `
        <div id="trading-lock-modal" class="trading-lock-modal">
            <div class="trading-lock-modal-content">
                <h2>Enter the code to access the Trading Course content</h2>
                <input type="text" id="trading-unlock-code" placeholder="Enter unlock code" tabindex="1">
                <button onclick="checkTradingUnlockCode()" tabindex="2">Unlock</button>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('afterbegin', modalHTML);

    document.getElementById("trading-unlock-code").addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            checkTradingUnlockCode();
        }
    });
};

const addTradingBlurredContentClass = () => {
    Array.from(document.body.children).forEach((child) => {
        if (child.id !== 'trading-lock-modal') {
            child.classList.add('trading-lock-blurred');
        }
    });
};

const checkTradingUnlockCode = () => {
    const enteredCode = document.getElementById("trading-unlock-code").value;
    const passhash = CryptoJS.SHA256(enteredCode).toString();
    const verified_code = "08c4242b5f585628bb8cef8ede40e9895b8719eb8070aee2d96613583ee3904a"; // sha256("stock")
    if (passhash === verified_code) {
        document.getElementById("trading-lock-modal").classList.add("trading-lock-hidden");
        Array.from(document.body.children).forEach((child) => {
            child.classList.remove('trading-lock-blurred');
        });
        document.cookie = "trading_unlocked=true; path=/; max-age=" + (60 * 60 * 24 * 30);
    } else {
        alert("Incorrect code. Please try again.");
    }
};

const checkTradingCookie = () => {
    const cookieValue = document.cookie.split("; ").find(row => row.startsWith("trading_unlocked="));
    if (cookieValue && cookieValue.split("=")[1] === "true") {
        document.getElementById("trading-lock-modal").classList.add("trading-lock-hidden");
        Array.from(document.body.children).forEach((child) => {
            child.classList.remove('trading-lock-blurred');
        });
    } else {
        addTradingBlurredContentClass();
        document.getElementById("trading-unlock-code").focus();
    }
};
