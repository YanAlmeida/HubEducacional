import UserForm from "../components/UserForm";

export default function Register() {
    return(
        <>
            <div className="container mt-5">
                <h1>Cadastro</h1>
                <div className="row">
                    <div className="col-sm-8">
                        <div className="card">
                            <div className="card-body">
                                <UserForm action="Cadastrar"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}