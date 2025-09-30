from Bio.Seq import Seq
"""
Notas: Por la forma en que Bio.seq, especificamente la funcion seq.translate maneja los codones
es posible que codones incompletos sean "rellenados" con N para poder seguir con el analisis, esto podria
no ser un nucleotido real, pero para explorar secuencias y no perder posibles codones me parece buena idea dejarlo
"""

# Secuencia de entrada (5' → 3')
dna_seq = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")

# Funcion para encontrar ORFs en un marco
def find_orfs_in_frame(seq: Seq, min_len=1):
    """
    Busca ORFs que empiezan con M y terminan con codon stop (*).
    Devuelve lista de proteinas completas.
    """
    proteins = []
    amino_seq = seq.translate(to_stop=False)
    proteina_temp = ""
    for aminos in amino_seq:
        if aminos == "M":
            proteina_temp = "M"      #variable temporal para ir escribiendo mis aminos
        elif aminos == "*":
            if len(proteina_temp) >= min_len:
                proteins.append(proteina_temp + "*")  # incluir stop
            proteina_temp = ""
        elif proteina_temp:
            proteina_temp += aminos
    return proteins  # solo ORFs terminados en stop

# Buscar ORFs en los 6 marcos
all_orfs = []
for strand, nuc in [("+", dna_seq), ("-", dna_seq.reverse_complement())]:
    for frame in range(3):
        subseq = nuc[frame:]
        prots = find_orfs_in_frame(subseq)
        for p in prots:
            all_orfs.append({
                "strand": strand,
                "frame": frame + 1,
                "protein": p,
                "length": len(p)
            })

# Filtrar ORFs vacios y ordenar por longitud
all_orfs = [orf for orf in all_orfs if len(orf["protein"]) > 0]
all_orfs.sort(key=lambda x: x["length"], reverse=True)

# Mostrar ORFs limpios
print(f"Se encontraron {len(all_orfs)} ORFs en todos los marcos:\n")
for i, orf in enumerate(all_orfs, 1):
    print(f"{i}. Hebra: {orf['strand']}, Frame: {orf['frame']}, Longitud: {orf['length']}")
    print(f"   Proteina: {orf['protein']}\n")

# Proteina mas larga
if all_orfs:
    print("Proteina mas larga encontrada:\n")
    print(all_orfs[0]["protein"])