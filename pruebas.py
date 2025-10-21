
class Envio():
    def __init__(self, cod_mon_origen, cod_mon_pago, id_pago, id_dest, nom_dest, tasa_conv, monto_nominal, alg_com, alg_imp):

        self.cod_mon_origen = int(cod_mon_origen)
        self.cod_mon_pago = int(cod_mon_pago)
        self.id_pago = id_pago
        self.id_dest = id_dest
        self.nom_dest = nom_dest
        self.tasa_conv = float(tasa_conv)
        self.monto_nominal = float(monto_nominal)
        self.alg_com = int(alg_com)
        self.alg_imp = int(alg_imp)

    def __str__(self):
        cadena = "Envio("
        cadena += "mon_origen=" + str(self.cod_mon_origen)
        cadena += ", mon_pago=" + str(self.cod_mon_pago)
        cadena += ", id_pago=" + self.id_pago
        cadena += ", id_dest=" + self.id_dest
        cadena += ", nom_dest=" + self.nom_dest
        cadena += ", tasa_conv=" + str(self.tasa_conv)
        cadena += ", monto_nominal=" + str(self.monto_nominal)
        cadena += ", alg_com=" + str(self.alg_com)
        cadena += ", alg_imp=" + str(self.alg_imp)
        cadena += ")"
        return cadena