import ListDocuments from "../../components/ListDocuments";
import Nav from "../../components/Nav";

export default function Documentos() {
    return(
        <>
            <Nav/>
            <div className="get-documents">
                <a className="btn btn-dark btn-lg" href="/documentos/post" role="button">Adicionar documento</a>
            </div>
            <ListDocuments/>
        </>
    )
}