import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import "../styles/RegisterForm.css";

function RegisterForm({ route, method }) {
    const [username, setUsername] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [phoneNumber, setPhoneNumber] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const data = method === "register"
                ? { username, first_name: firstName, last_name: lastName, email, password, phone_number: phoneNumber, confirm_password: confirmPassword }
                : { username, password };

            await api.post(route, data);

            navigate(method === "register" ? "/login" : "/");
        } catch (error) {
            alert("Ошибка: проверьте введённые данные");
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{method === "register" ? "Регистрация" : "Login"}</h1>
            <input
                className="form-input"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Логин"
                required
            />
            {method === "register" && (
                <>
                    <input
                        className="form-input"
                        type="text"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                        placeholder="Имя"
                        required
                    />
                    <input
                        className="form-input"
                        type="text"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                        placeholder="Фамилия"
                        required
                    />
                    <input
                        className="form-input"
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder="Почта"
                        required
                    />
                    <input
                        className="form-input"
                        type="tel"
                        value={phoneNumber}
                        onChange={(e) => setPhoneNumber(e.target.value)}
                        placeholder="Телефон"
                        required
                    />
                    <input
                        className="form-input"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Пароль"
                        required
                    />
                </>
            )}
            <input
                className="form-input"
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                placeholder="Подтвердите пароль"
                required
            />
            <button className="form-button" type="submit" disabled={loading}>
                {loading ? "Загрузка..." : method === "register" ? "Регистрация" : "Login"}
            </button>
        </form>
    );
}

export default RegisterForm;
