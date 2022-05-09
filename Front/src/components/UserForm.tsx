export default function UserForm(props) {
    return(
        <form action={props.action} method="POST">
            
            <div className="form-group">
                <label htmlFor="email">Email</label>
                <input type="email" className="form-control" name="username"/>
            </div>

            <div className="form-group">
                <label htmlFor="password">Password</label>
                <input type="password" className="form-control" name="password"/>
            </div>

            <button type="submit" className="btn btn-dark">Login</button>
        </form>
    )
}