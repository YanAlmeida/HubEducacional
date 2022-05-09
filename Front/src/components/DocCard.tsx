export default function DocCard(props) {
    return(
        <div className="doc-card">
            <h2>{props.doc.area_conhecimento}</h2>
            <p>Autor: {props.doc.autor}</p>
            <p>Tema: {props.doc.tema}</p>
            <p>Fonte: {props.doc.fonte}</p>
            <p>Path: {props.doc.file_path}</p>
        </div>
    )
}