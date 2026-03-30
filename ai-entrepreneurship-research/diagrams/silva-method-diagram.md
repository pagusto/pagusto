# DIAGRAMAS DEL METODO SILVA Y REPROGRAMACION MENTAL

---

## 1. PROCESO COMPLETO DEL METODO SILVA

```mermaid
flowchart TD
    A["INICIO<br/>Estado Beta Normal<br/>(14-30 Hz)"] --> B["PASO 1<br/>Relajacion Progresiva<br/>Cerrar ojos, respirar 3 veces"]
    B --> C["PASO 2<br/>Cuenta Regresiva<br/>De 10 a 1 (o 3 a 1)"]
    C --> D["PASO 3<br/>Profundizacion<br/>Visualizar lugar de paz"]
    D --> E{{"NIVEL ALFA<br/>Frecuencia 7-14 Hz<br/>Estado de Superaprendizaje"}}

    E --> F["OPCION A<br/>Espejo de la Mente<br/>Resolver Problemas"]
    E --> G["OPCION B<br/>Laboratorio Mental<br/>Consultar Asesores"]
    E --> H["OPCION C<br/>Tres Escenas<br/>Pasado-Presente-Futuro"]
    E --> I["OPCION D<br/>Programacion de Metas<br/>Visualizar Resultado"]

    F --> J["Visualizar problema<br/>en marco azul"]
    J --> K["Mover imagen a<br/>la izquierda"]
    K --> L["Visualizar solucion<br/>en marco blanco"]

    G --> M["Entrar al laboratorio<br/>mental personalizado"]
    M --> N["Invitar asesores<br/>(reales o imaginarios)"]
    N --> O["Hacer pregunta<br/>y recibir respuesta"]

    H --> P["Escena 1: Estado Actual<br/>(observar sin juzgar)"]
    P --> Q["Escena 2: Proceso<br/>(trabajando en solucion)"]
    Q --> R["Escena 3: Resultado<br/>(meta cumplida, sentir emocion)"]

    I --> S["Definir meta con<br/>fecha especifica"]
    S --> T["Visualizar con todos<br/>los sentidos"]
    T --> U["SENTIR la emocion<br/>como si ya ocurrio"]

    L --> V["SALIDA<br/>Contar de 1 a 5"]
    O --> V
    R --> V
    U --> V

    V --> W["ESTADO BETA<br/>Volver con energia<br/>y claridad"]

    style A fill:#3498db,stroke:#333,color:#fff
    style E fill:#FFD700,stroke:#333,color:#000,font-weight:bold
    style V fill:#2ecc71,stroke:#333,color:#fff
    style W fill:#2ecc71,stroke:#333,color:#fff
    style F fill:#e74c3c,stroke:#333,color:#fff
    style G fill:#9b59b6,stroke:#333,color:#fff
    style H fill:#e67e22,stroke:#333,color:#fff
    style I fill:#1abc9c,stroke:#333,color:#fff
```

---

## 2. PROTOCOLO DIARIO DE REPROGRAMACION MENTAL

```mermaid
flowchart TD
    subgraph MANANA["SESION MATUTINA (5:00 - 5:45 AM)"]
        A1["5:00 - Despertar<br/>No tocar telefono"] --> A2["5:05 - Respiracion Wim Hof<br/>30 respiraciones x 3 rondas"]
        A2 --> A3["5:15 - Meditacion Silva<br/>Entrar a Nivel Alfa"]
        A3 --> A4["5:25 - Afirmaciones<br/>en voz alta con emocion<br/>(Metodo Robbins)"]
        A4 --> A5["5:30 - Visualizacion<br/>Tu yo ideal en 5 anos<br/>(Metodo Dispenza)"]
        A5 --> A6["5:40 - Journaling<br/>3 gratitudes + intencion<br/>+ meta del dia"]
    end

    subgraph MEDIODIA["CHECK-IN MEDIODIA (12:00)"]
        B1["Pausa de 5 minutos"] --> B2["3 respiraciones<br/>profundas conscientes"]
        B2 --> B3["Reafirmar intencion<br/>del dia"]
        B3 --> B4["Calibrar energia<br/>Estoy en estado 10?"]
    end

    subgraph NOCHE["SESION NOCTURNA (9:30 - 10:00 PM)"]
        C1["9:30 - Revision<br/>Que logre hoy?<br/>Que aprendi?"] --> C2["9:35 - Perdon y Liberacion<br/>Soltar lo que no sirve"]
        C2 --> C3["9:40 - Metodo Silva<br/>Entrar a Nivel Alfa"]
        C3 --> C4["9:45 - Tecnica del Vaso de Agua<br/>Programar solucion<br/>para problema actual"]
        C4 --> C5["9:50 - Neville Goddard<br/>Sentir el deseo cumplido<br/>como si ya ocurrio"]
        C5 --> C6["9:55 - Afirmacion I AM<br/>(Wayne Dyer)<br/>Dormir en ese estado"]
    end

    MANANA --> MEDIODIA
    MEDIODIA --> NOCHE
    NOCHE --> |"El subconsciente<br/>procesa durante<br/>el sueno"| MANANA

    style MANANA fill:#1a1a2e,stroke:#FFD700,color:#FFD700
    style MEDIODIA fill:#16213e,stroke:#4ECDC4,color:#4ECDC4
    style NOCHE fill:#0f3460,stroke:#9b59b6,color:#e8d5f5
```

---

## 3. NIVELES DE CONSCIENCIA DE RIQUEZA

```mermaid
flowchart BT
    L1["NIVEL 1: ESCASEZ<br/>Mentalidad de victima<br/>El dinero es malo<br/>Yo no merezco riqueza"]
    L2["NIVEL 2: SUPERVIVENCIA<br/>Vivir de cheque en cheque<br/>Miedo constante<br/>Trabajar para pagar cuentas"]
    L3["NIVEL 3: ESTABILIDAD<br/>Ahorrar pero con miedo<br/>Seguridad como meta<br/>Evitar riesgos"]
    L4["NIVEL 4: CRECIMIENTO<br/>Invertir en uno mismo<br/>Tomar riesgos calculados<br/>Mentalidad de aprendizaje"]
    L5["NIVEL 5: ABUNDANCIA<br/>El dinero fluye con facilidad<br/>Crear valor masivo<br/>Multiples fuentes de ingreso"]
    L6["NIVEL 6: LIBERTAD<br/>El dinero trabaja para ti<br/>Tiempo es tu recurso<br/>Impacto global"]
    L7["NIVEL 7: TRASCENDENCIA<br/>Riqueza como vehiculo de servicio<br/>Ayudar a millones<br/>Legado generacional"]

    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 --> L5
    L5 --> L6
    L6 --> L7

    style L1 fill:#e74c3c,stroke:#333,color:#fff
    style L2 fill:#e67e22,stroke:#333,color:#fff
    style L3 fill:#f1c40f,stroke:#333,color:#000
    style L4 fill:#2ecc71,stroke:#333,color:#fff
    style L5 fill:#3498db,stroke:#333,color:#fff
    style L6 fill:#9b59b6,stroke:#333,color:#fff
    style L7 fill:#FFD700,stroke:#333,color:#000,font-weight:bold
```

---

## 4. ONDAS CEREBRALES Y TECNICAS ASOCIADAS

```mermaid
flowchart LR
    subgraph BETA["BETA (14-30 Hz)"]
        B1["Estado normal de vigilia"]
        B2["Pensamiento analitico"]
        B3["Estres, ansiedad"]
    end

    subgraph ALPHA["ALFA (7-14 Hz) - ZONA SILVA"]
        A1["Relajacion profunda"]
        A2["Superaprendizaje"]
        A3["Creatividad aumentada"]
        A4["Programacion mental"]
    end

    subgraph THETA["THETA (4-7 Hz) - ZONA DISPENZA"]
        T1["Meditacion profunda"]
        T2["Acceso al subconsciente"]
        T3["Sanacion y reprogramacion"]
        T4["Intuicion elevada"]
    end

    subgraph DELTA["DELTA (0.5-4 Hz)"]
        D1["Sueno profundo"]
        D2["Regeneracion celular"]
        D3["Neville Goddard:<br/>Programar antes de dormir"]
    end

    BETA -->|"Metodo Silva<br/>Cuenta regresiva<br/>10 a 1"| ALPHA
    ALPHA -->|"Dispenza<br/>Meditacion extendida<br/>45-60 min"| THETA
    THETA -->|"Transicion<br/>natural al sueno"| DELTA

    style BETA fill:#e74c3c,stroke:#333,color:#fff
    style ALPHA fill:#FFD700,stroke:#333,color:#000,font-weight:bold
    style THETA fill:#9b59b6,stroke:#333,color:#fff
    style DELTA fill:#2c3e50,stroke:#333,color:#fff
```

---

## 5. ARBOL DE DECISIONES - RUTINA MATUTINA

```mermaid
flowchart TD
    START["5:00 AM - DESPIERTO"] --> Q1{"Me siento<br/>con energia?"}

    Q1 -->|"Si"| E1["Respiracion Wim Hof<br/>(version intensa: 3 rondas)"]
    Q1 -->|"No"| E2["Respiracion suave<br/>4-7-8 (3 rondas)<br/>+ agua con limon"]

    E1 --> Q2{"Tengo un<br/>problema urgente?"}
    E2 --> Q2

    Q2 -->|"Si"| M1["Meditacion Silva:<br/>Espejo de la Mente<br/>o Vaso de Agua"]
    Q2 -->|"No"| M2{"Meta grande<br/>en progreso?"}

    M2 -->|"Si"| M3["Meditacion Silva:<br/>Tecnica Tres Escenas<br/>+ Visualizacion de meta"]
    M2 -->|"No"| M4["Meditacion Dispenza:<br/>Conectar con el<br/>campo cuantico"]

    M1 --> AFF["Afirmaciones<br/>(5 min con emocion)"]
    M3 --> AFF
    M4 --> AFF

    AFF --> Q3{"Dia de trabajo<br/>o descanso?"}

    Q3 -->|"Trabajo"| J1["Journaling:<br/>3 gratitudes<br/>+ Top 3 prioridades<br/>+ Intencion del dia"]
    Q3 -->|"Descanso"| J2["Journaling:<br/>3 gratitudes<br/>+ Reflexion semanal<br/>+ Lectura extendida"]

    J1 --> EX["Ejercicio 45 min"]
    J2 --> EX

    EX --> READ["Lectura 30 min"]
    READ --> GO["LISTO PARA<br/>CONQUISTAR EL DIA"]

    style START fill:#FFD700,stroke:#333,color:#000,font-weight:bold
    style GO fill:#2ecc71,stroke:#333,color:#fff,font-weight:bold
    style M1 fill:#3498db,stroke:#333,color:#fff
    style M3 fill:#3498db,stroke:#333,color:#fff
    style M4 fill:#9b59b6,stroke:#333,color:#fff
```

---

## 6. EL STACK DE HABILIDADES DEL EMPRESARIO IA

```mermaid
flowchart BT
    subgraph BASE["CAPA 1: INGENIERIA (Base Tecnica)"]
        B1["Python + APIs"]
        B2["Claude Code / IA"]
        B3["Automatizacion"]
        B4["Analisis de Datos"]
    end

    subgraph VENTAS["CAPA 2: VENTAS Y MARKETING"]
        V1["Copywriting"]
        V2["Funnels"]
        V3["Cold Outreach"]
        V4["Content Marketing"]
    end

    subgraph INFLUENCIA["CAPA 3: INFLUENCIA Y LIDERAZGO"]
        I1["Storytelling"]
        I2["Negociacion"]
        I3["Public Speaking"]
        I4["Networking"]
    end

    subgraph RIQUEZA["CAPA 4: CREACION DE RIQUEZA"]
        R1["Inversiones"]
        R2["Multiple Income"]
        R3["Scaling Systems"]
        R4["Asset Building"]
    end

    subgraph MAESTRIA["CAPA 5: MAESTRIA ESPIRITUAL"]
        M1["Meditacion"]
        M2["Visualizacion"]
        M3["Servicio"]
        M4["Legado"]
    end

    BASE --> VENTAS
    VENTAS --> INFLUENCIA
    INFLUENCIA --> RIQUEZA
    RIQUEZA --> MAESTRIA

    style BASE fill:#3498db,stroke:#333,color:#fff
    style VENTAS fill:#e67e22,stroke:#333,color:#fff
    style INFLUENCIA fill:#2ecc71,stroke:#333,color:#fff
    style RIQUEZA fill:#FFD700,stroke:#333,color:#000
    style MAESTRIA fill:#9b59b6,stroke:#333,color:#fff
```

---

> **Nota**: Visualiza estos diagramas en GitHub, Obsidian, VS Code (extension Mermaid), o [mermaid.live](https://mermaid.live).
