<style>
/* ─── Sidebar ───────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    width: 230px;
    min-width: 200px;
    border-right: 3px solid #FF7F66;
    background-color: #fff;
}

/* ─── Mobile menu button ────────────────────────────────── */
.menu-indicator {
    display: none;
}

@media (max-width: 1024px) {
    .menu-indicator {
        display: flex;
        align-items: center;
        justify-content: center;
        position: fixed;
        top: 1rem;
        left: 1rem;
        background-color: #FF4500;
        color: #fff;
        font-weight: 700;
        font-size: 1.2rem;
        padding: 0.8rem 1rem;
        border-radius: 50px;
        cursor: pointer;
        z-index: 9999;
        box-shadow: 0 4px 10px rgba(0,0,0,0.25);
        border: 2px solid white;
        animation: pulse 1.5s infinite;
    }
}

/* ─── Pulse animation ───────────────────────────────────── */
@keyframes pulse {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 69, 0, 0.6); }
    50% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(255, 69, 0, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 69, 0, 0); }
}
</style>
<div class="menu-indicator">☰ MENU</div>
