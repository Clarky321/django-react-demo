import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Header.css";

function Header({ username }) {
    const [menuOpen, setMenuOpen] = useState(false);
    const navigate = useNavigate();

    const handleLogout = () => {
        // Очистка токенов из локального хранилища
        localStorage.removeItem("ACCESS_TOKEN");
        localStorage.removeItem("REFRESH_TOKEN");
        navigate("/login");
    };

    const toggleMenu = () => {
        setMenuOpen((prev) => !prev);
    };

    return (
        <header className="header">
            <div className="app-icon"> {/* Здесь можно добавить иконку приложения */}
                <img src="../assets/icons1.ico" alt="logo" className="logo" />
                <span className="app-name">САЙТ</span>
            </div>
            <div className="user-section" onClick={toggleMenu}>
                <span className="username">{username}</span>
                {menuOpen && (
                    <div className="dropdown-menu">
                        <button onClick={() => navigate("/profile")}>Личный кабинет</button>
                        <button onClick={handleLogout}>Выйти</button>
                    </div>
                )}
            </div>
        </header>
    );
}

export default function HomeForm() {
    const username = localStorage.getItem("USERNAME") || "Guest"; // Получаем имя пользователя

    return (
        <div>
            <Header username={username} />
            {/* Дополнительный контент главной страницы */}
        </div>
    );
}