from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedidos
import modules.getPagos as pago
#print(tabulate(oficina.getAllCiudadTelefono('Australia')))

print(tabulate(pago.getAllPagosFecha(), tablefmt="grid"))
#print(tabulate(pago.getAllCodigoClienteFecha()))
