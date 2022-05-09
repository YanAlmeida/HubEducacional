export default function Home() {
    return(
            <div className="jumbotron centered">
                <div className="container">
                    <i className="fas fa-graduation-cap fa-6x"></i>
                    <h1 className="display-3">Hub Educacional</h1>
                    <p className="lead">Organizando os estudos dos alunos da UFABC</p>
                    <hr/>
                    <a className="btn btn-light btn-lg" href="/register" role="button">Register</a>
                    <a className="btn btn-dark btn-lg" href="/login" role="button">Login</a>
                </div>
            </div>
    )
}