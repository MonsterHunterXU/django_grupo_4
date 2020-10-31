function confirmDelete(nombreinsumo) {
  Swal.fire({ title: "Estás seguro?", 
  text: "No podrás deshacer esta acción!", 
  icon: "warning", 
  showCancelButton: true, 
  confirmButtonColor: "#3085d6", 
  confirmButtonText: "Si, Eliminar!", 
  cancelButtonColor: "#d33", 
  cancelButtonText: "Cancelar" }).then((result) => { if (result.value) 
    { Swal.fire("Eliminado!", "Empleado Eliminado Correctamente!", "success").then(function () 
    { window.location.href = "/eliminarinsumo/" + id + "/"; }) } });
}