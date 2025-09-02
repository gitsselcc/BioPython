

class gen():
    def __init__(self, nombre, ubicacion, secuencia,tipo):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.secuencia = secuencia.upper()
        self.tipo = tipo
    def cant_t(self):
        return self.secuencia.count("T")
    def longitud(self):
        return len(self.secuencia)
    def GC_porcentaje(self):
        gc = self.secuencia.count('G') + self.secuencia.count('C')
        return (gc / len(self.secuencia)) * 100
    def secuencia_reversa(self):
        return self.secuencia[::-1]

class trna(gen):
    def __init__(self, nombre, ubicacion, secuencia, tipo ,anticodon):
        super().__init__(nombre,ubicacion ,secuencia, tipo)
        self.anticodon = anticodon

    def validar_codon(self):
        return len(self.anticodon) == 3
   
    def longitud(self):
        return len(self.secuencia)   
    

class rna_nocod (gen):
    def __init__(self, nombre, ubicacion, secuencia,tipo,estructura):
        super().__init__(nombre, ubicacion, secuencia, tipo)
        self.estructura=estructura

    def sec_corta(self):
        return len(self.secuencia)<200


class proteina(trna):
    def __init__(self, nombre, ubicacion, secuencia, tipo, anticodon, peso_mol):
        super().__init__(nombre, ubicacion, secuencia, tipo, anticodon)
        self.peso_mol = peso_mol

    def alto_peso(self):
        return self.peso_mol > 100   
    
    def longitud(self):
        nt = len(self.secuencia)             # nucleotidos
        aa = nt // 3                         # aminoacidos 
        return f"Nucleotidos: {nt}, Aminoacidos: {aa}"


g1 = gen("gen muy extraño", "chamilpa", "ATGCGTACGTAGCTAGCTAG", "gen")
t1 = trna("tRNA-Trex", "cromosoma i""AUGGCCAUUGUAAUGGGCCGCUUAA", "trna", "UAA")
n1 = rna_nocod("regulon nuevo", "UAEM", "AUCGGAUUGCGCUAGC", "noncodrna", "loop")
p1 = proteina("Sonic the Heahdog", "cromosoma 4", "GGCCAUUGUAAUGGGCCGCUUAA", "proteina", "CCC", 250)

print("=== Gene ===")
print("Nombre:", g1.nombre, "| Ubicacion:", g1.ubicacion, "| Secuencia:", g1.secuencia, "| Tipo:", g1.tipo)
print("Cantidad de T:", g1.cant_t(), "| Longitud:", g1.longitud(), "| GC%:", g1.GC_porcentaje())
print("Secuencia reversa:", g1.secuencia_reversa())

print("\n=== tRNA ===")
print("Nombre:", t1.nombre, "| Ubicacion:", t1.ubicacion, "| Secuencia:", t1.secuencia, "| Tipo:", t1.tipo)
print("Anticodon:", t1.anticodon, "| Valido:", t1.validar_codon(), "| Longitud:", t1.longitud())

print("\n=== RNA no codificante ===")
print("Nombre:", n1.nombre, "| Ubicacion:", n1.ubicacion, "| Secuencia:", n1.secuencia, "| Tipo:", n1.tipo)
print("Estructura:", n1.estructura, "| Secuencia corta:", n1.sec_corta(), "| Longitud:", n1.longitud())

print("\n=== Proteina ===")
print("Nombre:", p1.nombre, "| Ubicacion:", p1.ubicacion, "| Secuencia:", p1.secuencia, "| Tipo:", p1.tipo)
print("Anticodon:", p1.anticodon, "| Peso molecular:", p1.peso_mol, "| Alto peso:", p1.alto_peso())
print("Longitud (nueva):", p1.longitud())
