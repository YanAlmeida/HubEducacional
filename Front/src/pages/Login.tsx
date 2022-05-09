import UserForm from "../components/UserForm"

export default function Login() {
    return(
        <>
            <div className="container mt-5">
                <h1>Login</h1>

                <div className="row">
                    <div className="col-sm-8">
                        <div className="card">
                            <div className="card-body">
                                <UserForm action="/login"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}