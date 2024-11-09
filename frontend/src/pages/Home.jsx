import HomeForm from "../components/HomeForm"

function Home() {
    return (
        <div>
            <HomeForm /> {/* Включаем компонент HomeForm для отображения шапки */}
            <div>Главная страница</div>
        </div>
    );
}

export default Home;