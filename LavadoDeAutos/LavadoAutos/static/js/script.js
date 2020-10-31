var arregloC = new Array();
var indice = 0;

/Funcion para guardar formulario en el local storage/
function grabar() {
    var nombre = document.getElementById("txtNombre").value;
    var apellido = document.getElementById("txtApellido").value;
    var email = document.getElementById("txtEmail").value;
    var fechaNacimiento = document.getElementById("txtfecha").value;
    var usuario = document.getElementById("txtUsuario").value;
    var contraseña = document.getElementById("txtContraseña").value;
    var repetircontraseña = document.getElementById("txtRepetirContraseña").value;
    cli = new Cliente();
    cli.setNombre(nombre);
    cli.setApellido(apellido);
    cli.setEmail(email);
    cli.setFechaNacimiento(fechaNacimiento);
    cli.setUsuario(usuario);
    cli.setContraseña(contraseña);
    cli.setRepetirContraseña(repetircontraseña)
    arregloC[indice] = JSON.stringify(cli);
    indice++;
    localStorage.setItem("Registro Clientes", arregloC);
    alert("Cuenta Creada Exitosamente");
}

/*/Funcion para validar el digito verificador/
function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        alert("Rut no tiene el largo necesario");
        return false;
    }
    var num = 3;
    var sum = 0;
    for (let index = 0; index < 8; index++) {
        var carac = rut.slice(index, index + 1);
        sum = sum + (carac * num);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = sum % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        alert("Rut incorrecto")
        return false;
    } else {
        return true;
    }
}
*/

/validaciones registros/
function validarNombre() 
{
    var n = document.getElementById("txtNombre").value;
    if (n.trim().length == "")
    {
        alert("Ingrese su Nombre")
        return false;
    }
}

function validarApellido() 
{
    var n = document.getElementById("txtApellido").value;
    if (n.trim().length == "")
    {
        alert("Ingrese su Apellido")
        return false;
    }
}

function validarUsuario() 
{
    var n = document.getElementById("txtUsuario").value;
    if (n.trim().length == "")
    {
        alert("Ingrese Usuario")
        return false;
    }
}

function validarContraseña() 
{
    var n = document.getElementById("txtContraseña").value;
    if (n.trim().length == "")
    {
        alert("Ingrese Contraseña")
        return false;
    }
}

function validarContrasena(){
    var contraseña = document.getElementById("txtContraseña").value;
    var repetirContraseña = document.getElementById("txtRepetirContraseña").value;

    if(contraseña==repetirContraseña){
        
        alert("contraseña validada");
        return true;

    }

    else{
        
        alert("las contraseñas no considen")
        return false;
    }
}

/*/Funcion para validad fecha/
function validarFecha() {
    var fechaForm = document.getElementById("txtfecha").value;
    var fechaSistema = new Date();
    var ano = fechaForm.slice(0, 4);
    var mes = fechaForm.slice(5, 7);
    var dia = fechaForm.slice(8, 10);
    var fechaMia = new Date(ano, mes - 1, dia);
    if (fechaMia > fechaSistema) {
        alert("Fecha de nacimiento Incorrecto");
        return false;
    }
    return true;
}
*/

/Validar Registro de Insumos/
class Producto {
    nombre;
    precio;
    descripcion;

    setNombre(nombre) { this.nombre = nombre; }
    setPrecio(precio) { this.precio = precio; }
    setDescripcion(descripcion) { this.descripcion = descripcion; }

    getNombre() { return this.nombre; }
    getPrecio() { return this.precio; }
    getDescripcion() { return this.descripcion; }
}

var arregloP = new Array();
var indice = 0;

/Funcion para guardar producto en el local storage/
function grabarProducto() {
    var nombre = document.getElementById("txtNombreInsumo").value;
    var precio = document.getElementById("txtPrecio").value;
    var descripcion = document.getElementById("txtDescripcion").value;
    pro = new Producto();
    pro.setNombre(nombre);
    pro.setPrecio(precio);
    pro.setDescripcion(descripcion);
    arregloP[indice] = JSON.stringify(pro);
    indice++;
    localStorage.setItem("Registro Producto", arregloP);
    alert("Producto Guardo Exitosamente");
}

/Validaciones Registro de insumos/
function validarNombreInsumo() 
{
    var n = document.getElementById("txtNombreInsumo").value;
    if (n.trim().length == "")
    {
        alert("Ingrese Nombre del Insumo")
        return false;
    }
}

function validarPrecio() 
{
    var n = document.getElementById("txtPrecio").value;
    if (n.trim().length == "")
    {
        alert("Ingrese Precio")
        return false;
    }
}

function validarStock() 
{
    var n = document.getElementById("txtStock").value;
    if (n.trim().length == "")
    {
        alert("Ingrese Stock")
        return false;
    }
}

/Validar todos los input Registro/
function validarTodo() {
    var resp;
    resp = validarNombre();
    if (resp == false) 
    {
        return false;
    }
    resp = validarApellido();
    if (resp == false) 
    {
        return false;
    }
    resp = validarUsuario();
    if (resp == false) 
    {
        return false;
    }
    resp = validarContraseña();
    if (resp == false) 
    {
        return false;
    }
    resp = validarContrasena();
    if (resp == false) {
        return false;
    }
    grabar();
    return true;
}

function validarInsumos()
{
    var resp;

    resp = validarNombreInsumo();
    if (resp == false) 
    {
        return false;
    }

    resp = validarPrecio();
    if (resp == false) 
    {
        return false;
    }
    resp = validarStock();
    if (resp == false) 
    {
        return false;
    }
    grabarProducto();
    return true;

}
