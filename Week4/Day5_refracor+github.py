"""
Refactoring means improving existing code without changing what it does. Today you go back to your best
scripts from Weeks 1-3 and add proper error handling. This is what separates a script that works on your
machine from one that works in production.
"""
"""
Week 1 — calculadora_financiera.py
  → Add try/except around float conversions
  → Validate that salario_cop > 0 before calculating

Week 2 — ProyectoSemana2_Analizador.py
  → Handle empty lists in promedio_variable()
  → Validate that municipios list is not empty

Week 3 — ProjectWeek3_Pipeline.py
  → Wrap the entire pipeline in try/except
  → Log errors with timestamp
  → Handle missing columns in the CSV gracefully
"""
#Week1
def safe_convert(value, default=0):
    """Safely converts a value to float salary."""
    try:
        result = float(str(value).replace(",", "").strip())
        return result if result > 0 else default
    except (ValueError, TypeError):
        return default

# 1. cop_a_usd(monto, tasa=4200)      ← Día 1
def cop_a_usd(monto_cop, tasa=4200):
    return round(monto_cop / tasa, 2)

# 2. calcular_cuota(monto, tasa, meses) ← Día 2
def calcular_cuota(monto, mes, tasa_mensual=0.018):
    cuota = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -mes)
    return round(cuota, 2)

# 3. retencion = lambda s: ...         ← Día 4
def calcular_retencion(salario_usd, tasa_ret=0.04):
    return round(salario_usd * tasa_ret, 2) if salario_usd > 750 else 0

def resumen_empleado(nombre, **datos):
    """
    Recibe nombre y datos variables del empleado.
    Imprime un resumen financiero completo usando
    las funciones anteriores.
    """
    salario = safe_convert(datos.get("salario_cop", 0))
    meses = safe_convert(datos.get("meses_credito", 0))
    prestamo = safe_convert(datos.get("prestamo_usd", 0))

    salario_usd = cop_a_usd(salario)
    retenido = calcular_retencion(salario_usd, tasa_ret=0.04)
    cuota = calcular_cuota(prestamo, meses)
    neto = cop_a_usd(salario) - retenido - cuota

    print(f"\n=== Resumen financiero: {nombre} ===")
    print(f"Salario COP:     ${salario:,.0f}")
    print(f"Salario USD:     ${salario_usd:,.2f}")
    print(f"Retención 4% USD:    ${retenido:,.2f}")
    print(f"Cuota crédito USD:   ${cuota:,.2f}")
    print(f"Final neto USD:      ${neto:,.2f}")

empleados = [
    {
        "nombre": "Felipe",
        "salario_cop": "10000000",
        "meses_credito": 12,
        "prestamo_usd": 5000,
    },
    {
        "nombre": "Laura",
        "salario_cop": 4200000 ,
        "meses_credito": 24,
        "prestamo_usd": 2000,
    },
    {
        "nombre": "Carlos",
        "salario_cop": 7500000,
        "meses_credito": 6,
        "prestamo_usd": "1000",
    },
]
for empleado in empleados:
    resumen_empleado(**empleado)

#WEEK2
def safe_pib_or_population(value, default=0):
    """Safely converts a value to float salary."""
    try:
        result = float(str(value).replace(",", "").strip())
        return result if result > 0 else default
    except (ValueError, TypeError):
        return default

def clean_city_row(row):
    """Cleans and validates a single city row."""
    return {
        "municipio": str(row.get("municipio", "")).strip() or "Unknown",
        "departamento": str(row.get("departamento", "")).strip() or "Unknown",
        "poblacion": safe_pib_or_population(row.get("poblacion"), default=0),
        "pib_per_capita": safe_pib_or_population(row.get("pib_per_capita"), default=0),
    }

municipios = [
    ("Bogotá", "Cundinamarca", "8000000", 28000000),
    ("Medellín", "", 2500000, 22000000),
    ("Cali", "Valle del Cauca", 2200000, 15000000),
    ("Barranquilla", "Atlántico", 1200000, 18000000),
    ("Bucaramanga", "Santander", 600000, 19000000),
    ("Cartagena", "Bolívar", 1000000, 14000000),
    ("Cúcuta", "Norte de Santander", 750000, 11000000),
    ("Pereira", "Risaralda", 480000, 16000000),
    ("Manizales", "Caldas", 420000, 17000000),
    ("Ibagué", "Tolima", 560000, 12000000),
]
# (municipio, departamento, poblacion, pib_per_capita)
municipios_limpio = []
for m in municipios:
    row = {"municipio" : m[0],
           "departamento" : m[1],
           "poblacion" : m[2],
           "pib_per_capita" : m[3],
    }
    municipios_limpio.append(clean_city_row(row))

#1 Dict comprehension → {municipio: poblacion} para todos
mun_pob = {m["municipio"]: m["poblacion"] for m in municipios_limpio}

#2 List comprehension → municipios con PIB per cápita mayor al promedio
pib = [m["pib_per_capita"] for m in municipios_limpio]
prom_pib = sum(pib)/len(pib)

#3 Set → departamentos únicos representados en la lista
dept = {m["departamento"] for m in municipios_limpio}

#4 Tuplas + max() → top 3 municipios por población usando sorted()
top_pob = sorted(mun_pob.items(), key=lambda x: x[1], reverse=True)
top3 = top_pob[:3]

print("=== Analizador de Municipios en Colombia ===")
print(f"Total ciudades: {len(municipios)}")
print(f"Total departamentos unicos: {len(dept)}")
print(f"Municipios sobre el PIB promedio ({prom_pib:,.0f}):")
for m in municipios_limpio:
    if m["pib_per_capita"] > prom_pib:
        print(f"- {m['municipio']}")
print("Top 3 por población")
for i, (municipio,poblacion) in enumerate(top3, start=1):
    print(f"{i}. {municipio}:     {poblacion:,.0f} hab.")

#WEEK3
"""
Colombian cities data pipeline.
Reads raw CSV, enriches it with calculations,
saves a timestamped JSON report, logs each step.
"""

# 1. Read week3_day1_colombian_cities.csv
# 2. Add calculated columns:
#    - salary_usd = avg_salary_cop / 4200
#    - category = "major" if population > 1M else "minor"
# 3. Filter: only cities where salary_usd > 500
# 4. Save filtered results to week3_output/report_TIMESTAMP.json
# 5. Print a summary: total cities read, cities after filter,
#    output filename, timestamp of run

import csv, json, os
from datetime import datetime

class DataValidationErrorExercise(Exception):
    """Raised when data doesn't meet validation requirements."""
    pass

def log_error(error_type, error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {error_type}: {error}")

def safe_pib_or_population(value, default=0):
    try:
        cleaned = str(value).strip()
        # Detects colombian format: 600.000 → 600000
        if "." in cleaned and len(cleaned.split(".")[-1]) == 3:
            print(f"[WARNING] Converted Colombian format: {value} → {cleaned.replace('.', '')}")
            cleaned = cleaned.replace(".", "")
        result = float(cleaned.replace(",", ""))
        return result if result > 0 else default
    except (ValueError, TypeError):
        return default

def clean_city_row(row):
    population = safe_pib_or_population(row.get("population"), default=None)
    salary = safe_pib_or_population(row.get("avg_salary_cop"), default=None)

    if population is None:
        raise DataValidationErrorExercise(f"Invalid population in row: {row.get('city')}")
    if salary is None:
        raise DataValidationErrorExercise(f"Invalid salary in row: {row.get('city')}")

    return {
        "city": str(row.get("city", "")).strip() or "Unknown",
        "department": str(row.get("department", "")).strip() or "Unknown",
        "population": population,
        "avg_salary_cop": salary,
    }

def run_pipeline(input_file, output_folder):
    """
    Reads a CSV, transforms the data,
    saves results as a timestamped JSON file.
    """
    # Step 1 — Read
    with open(input_file, "r", encoding="utf-8") as f:
        raw_data = list(csv.DictReader(f))

    # Step 2 — Clean con log de errores
    data=[]
    for row in raw_data:
        try:
            cleaned = clean_city_row(row)
            data.append(cleaned)
        except Exception as e:
            log_error("CLEAN ERROR", e)

    # Step 3 — Transform
    for row in data:
        row["salary_usd"] = round(float(row["avg_salary_cop"]) / 4200, 2)
        row["category"] = "major" if int(row["population"]) > 100000 else "minor"

    # Step 4 — Filter
    results = [row for row in data if row["salary_usd"] > 500]

    # Step 5 — Save
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"report_{timestamp}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    # Step 6 — Log
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Pipeline done\n"
          f"Cities read: {len(raw_data)}\n"
          f"Cities cleaned: {len(data)}\n"
          f"Cities after filter: {len(results)}\n"
          f"Cities skipped: {len(raw_data)-len(data)}\n"
          f"Records saved to {output_path}")

run_pipeline("week3_day1_colombian_cities.csv", "week4_output")

