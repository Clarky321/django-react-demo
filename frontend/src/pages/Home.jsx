import HomeForm from "../components/HomeForm"

function Home() {
    return (
        <div>
            <HomeForm /> {/* Включаем компонент HomeForm для отображения шапки */}
            <div>Добро пожаловать на главную страницу</div>
        </div>
    );
}

export default Home;