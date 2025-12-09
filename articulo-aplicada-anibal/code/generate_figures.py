#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Gráficas para Plantilla LaTeX - Ingeniería de Software
Genera gráficas de ejemplo relacionadas con DevOps, metodologías ágiles y métricas DORA
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
import os

# Configuración global para mejorar la calidad de las gráficas
plt.style.use('default')
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 9
rcParams['figure.titlesize'] = 13
rcParams['savefig.dpi'] = 300
rcParams['savefig.bbox'] = 'tight'
rcParams['savefig.pad_inches'] = 0.1

# Crear directorio de gráficas si no existe
graphics_dir = 'graphics'
os.makedirs(graphics_dir, exist_ok=True)

def generar_metricas_dora():
    """Genera gráfica de barras con métricas DORA por equipo"""
    
    # Datos de ejemplo: métricas DORA por equipo
    equipos = ['Equipo Alpha', 'Equipo Beta', 'Equipo Gamma', 'Equipo Delta']
    deployment_freq = [15.2, 8.7, 22.1, 12.4]  # deployments por semana
    lead_time = [2.1, 4.8, 1.3, 3.2]  # días
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfica 1: Frecuencia de Deployment
    bars1 = ax1.bar(equipos, deployment_freq, color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'])
    ax1.set_title('Frecuencia de Deployment por Equipo')
    ax1.set_ylabel('Deployments por semana')
    ax1.set_ylim(0, 25)
    
    # Añadir valores en las barras
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}', ha='center', va='bottom')
    
    # Gráfica 2: Lead Time
    bars2 = ax2.bar(equipos, lead_time, color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'])
    ax2.set_title('Lead Time por Equipo')
    ax2.set_ylabel('Días promedio')
    ax2.set_ylim(0, 6)
    
    # Añadir valores en las barras
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/metricas_dora.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/metricas_dora.png', format='png')
    plt.close()
    print("✓ Generada: metricas_dora.pdf/png")

def generar_evolucion_temporal():
    """Genera gráfica de líneas mostrando evolución temporal de métricas"""
    
    # Datos de ejemplo: evolución mensual
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']
    cobertura_pruebas = [68, 72, 75, 78, 82, 85, 87, 89, 91, 93, 94, 95]
    defectos_produccion = [28, 25, 22, 19, 16, 14, 12, 10, 8, 6, 5, 4]
    velocidad_equipo = [32, 35, 38, 42, 45, 48, 52, 55, 58, 61, 63, 65]
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Eje Y izquierdo: Cobertura y Velocidad
    color = '#2E86AB'
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Cobertura de Pruebas (%) / Velocidad (Story Points)', color=color)
    line1 = ax1.plot(meses, cobertura_pruebas, color=color, marker='o', linewidth=2, 
                     label='Cobertura de Pruebas (%)')
    line2 = ax1.plot(meses, velocidad_equipo, color='#F18F01', marker='s', linewidth=2, 
                     label='Velocidad del Equipo (SP)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 100)
    
    # Eje Y derecho: Defectos
    ax2 = ax1.twinx()
    color = '#C73E1D'
    ax2.set_ylabel('Defectos en Producción', color=color)
    line3 = ax2.plot(meses, defectos_produccion, color=color, marker='^', linewidth=2, 
                     label='Defectos en Producción')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 30)
    
    # Leyenda combinada
    lines = line1 + line2 + line3
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='center right')
    
    plt.title('Evolución de Métricas de Calidad del Software (2024)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/evolucion_metricas.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/evolucion_metricas.png', format='png')
    plt.close()
    print("✓ Generada: evolucion_metricas.pdf/png")

def generar_correlacion_practicas():
    """Genera gráfica de dispersión mostrando correlación entre prácticas DevOps"""
    
    np.random.seed(42)  # Para reproducibilidad
    
    # Datos simulados: correlación entre automatización y performance
    n_equipos = 25
    automatizacion = np.random.normal(70, 15, n_equipos)
    automatizacion = np.clip(automatizacion, 20, 95)
    
    # Correlación positiva con algo de ruido
    performance = 0.8 * automatizacion + np.random.normal(0, 8, n_equipos) + 10
    performance = np.clip(performance, 30, 100)
    
    # Tamaños basados en el tamaño del equipo
    team_sizes = np.random.randint(3, 15, n_equipos)
    
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(automatizacion, performance, s=team_sizes*10, 
                         c=team_sizes, cmap='viridis', alpha=0.7, edgecolors='black', linewidth=0.5)
    
    # Línea de tendencia
    z = np.polyfit(automatizacion, performance, 1)
    p = np.poly1d(z)
    plt.plot(automatizacion, p(automatizacion), "--", color='red', linewidth=2, alpha=0.8)
    
    plt.xlabel('Nivel de Automatización (%)')
    plt.ylabel('Performance del Equipo (índice)')
    plt.title('Correlación entre Automatización y Performance del Equipo')
    
    # Colorbar para tamaño del equipo
    cbar = plt.colorbar(scatter)
    cbar.set_label('Tamaño del Equipo (personas)')
    
    # Añadir estadísticas
    correlation = np.corrcoef(automatizacion, performance)[0,1]
    plt.text(0.05, 0.95, f'Correlación: r = {correlation:.3f}', 
             transform=plt.gca().transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/correlacion_devops.pdf', format='pdf')
    plt.savefig(f'{graphics_dir}/correlacion_devops.png', format='png')
    plt.close()
    print("✓ Generada: correlacion_devops.pdf/png")

def generar_comparacion_metodologias():
    """Genera gráfica de radar comparando metodologías ágiles"""
    
    # Datos para comparación de metodologías
    categorias = ['Flexibilidad', 'Velocidad\nEntrega', 'Calidad\nCódigo', 'Satisfacción\nCliente', 
                  'Gestión\nRiesgos', 'Escalabilidad']
    
    # Puntuaciones (1-10) para cada metodología
    scrum_scores = [8, 9, 7, 9, 6, 7]
    kanban_scores = [9, 7, 8, 8, 8, 8]
    xp_scores = [7, 8, 10, 7, 7, 6]
    
    # Configurar gráfica de radar
    angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
    angles += angles[:1]  # Cerrar el círculo
    
    scrum_scores += scrum_scores[:1]
    kanban_scores += kanban_scores[:1]
    xp_scores += xp_scores[:1]
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    # Dibujar las líneas para cada metodología
    ax.plot(angles, scrum_scores, 'o-', linewidth=2, label='Scrum', color='#2E86AB')
    ax.fill(angles, scrum_scores, alpha=0.25, color='#2E86AB')
    
    ax.plot(angles, kanban_scores, 's-', linewidth=2, label='Kanban', color='#F18F01')
    ax.fill(angles, kanban_scores, alpha=0.25, color='#F18F01')
    
    ax.plot(angles, xp_scores, '^-', linewidth=2, label='XP', color='#C73E1D')
    ax.fill(angles, xp_scores, alpha=0.25, color='#C73E1D')
    
    # Configurar etiquetas y límites
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categorias)
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.set_yticklabels(range(0, 11, 2))
    ax.grid(True)
    
    plt.title('Comparación de Metodologías Ágiles', size=14, y=1.08)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    plt.tight_layout()
    plt.savefig(f'{graphics_dir}/comparacion_metodologias.pdf', format='pdf', bbox_inches='tight')
    plt.savefig(f'{graphics_dir}/comparacion_metodologias.png', format='png', bbox_inches='tight')
    plt.close()
    print("✓ Generada: comparacion_metodologias.pdf/png")

def generar_tabla_frameworks():
    """Genera una tabla LaTeX con comparación de frameworks"""
    
    tabla_latex = r"""
\begin{table}[htbp]
\centering
\caption{Comparación de Frameworks de Desarrollo Web}
\label{tab:frameworks}
\begin{tabular}{lccccc}
\toprule
\textbf{Framework} & \textbf{Lenguaje} & \textbf{Performance} & \textbf{Curva Aprendizaje} & \textbf{Comunidad} & \textbf{Puntuación} \\
\midrule
React & JavaScript & Alta & Media & Excelente & 9.2 \\
Angular & TypeScript & Alta & Alta & Excelente & 8.7 \\
Vue.js & JavaScript & Alta & Baja & Buena & 8.9 \\
Django & Python & Media & Media & Excelente & 8.5 \\
Spring Boot & Java & Alta & Alta & Excelente & 8.8 \\
Laravel & PHP & Media & Baja & Buena & 8.1 \\
Express.js & JavaScript & Alta & Baja & Buena & 8.3 \\
\bottomrule
\end{tabular}
\end{table}
"""
    
    # Guardar tabla en archivo
    with open(f'tables/frameworks_comparison.tex', 'w', encoding='utf-8') as f:
        f.write(tabla_latex.strip())
    
    print("✓ Generada: frameworks_comparison.tex")

def main():
    """Función principal para generar todas las gráficas"""
    print("🎨 Generando gráficas para plantilla LaTeX...")
    print("=" * 50)
    
    try:
        generar_metricas_dora()
        generar_evolucion_temporal()
        generar_correlacion_practicas()
        generar_comparacion_metodologias()
        generar_tabla_frameworks()
        
        print("=" * 50)
        print("✅ ¡Todas las gráficas y tablas fueron generadas exitosamente!")
        print("\nArchivos generados:")
        print("📊 Gráficas PDF (para LaTeX): graphics/")
        print("🖼️  Gráficas PNG (para vista previa): graphics/")
        print("📋 Tabla LaTeX: tables/frameworks_comparison.tex")
        
    except Exception as e:
        print(f"❌ Error al generar gráficas: {e}")
        raise

if __name__ == "__main__":
    main()