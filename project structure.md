# Flight Delay Prediction — Professional Architecture Overview

```mermaid
flowchart LR

    %% Layer 1: User interaction
    subgraph UX["1. User Experience"]
        U(["✈️ Flight User"])
        A["📱 Streamlit App<br/>Python entry point<br/><b>app.py</b>"]
        I["📝 Flight Details"]
        P["📊 Delay Prediction"]
    end

    %% Layer 2: Feature preparation
    subgraph FEAT["2. Feature Pipeline"]
        F["🔢 Feature Vector"]
        S["📋 Feature Schema<br/><b>feature_names.pkl</b>"]
    end

    %% Layer 3: Model inference
    subgraph ML["3. Prediction Layer"]
        D["🤖 Departure Delay Model<br/><b>XGBoost Regressor</b>"]
        R["🤖 Arrival Delay Model<br/><b>XGBoost Regressor</b>"]
    end

    %% Layer 4: Training and delivery
    subgraph OPS["4. Training & Deployment"]
        N["📓 Training Notebook<br/><b>airlines pred.ipynb</b>"]
        REQ["📦 Dependencies<br/><b>requirements.txt</b>"]
        DOCKER["🐳 Container Image<br/><b>Dockerfile</b>"]
        CI["⚙️ GitHub Actions<br/><b>CI/CD Pipeline</b>"]
    end

    %% Core workflow
    U --> A
    A --> I
    I --> F
    S --> F
    A --> S
    F --> D
    F --> R
    D --> P
    R --> P
    P --> A

    %% Training and artifact lifecycle
    N -. trains .-> D
    N -. trains .-> R
    N -. generates .-> S
    REQ -. configures .-> A
    DOCKER --> A
    DOCKER --> D
    DOCKER --> R
    DOCKER --> REQ
    CI --> DOCKER

    %% Styling
    classDef user fill:#F8FAFC,stroke:#475569,stroke-width:2px,color:#0F172A;
    classDef ui fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#172554;
    classDef feature fill:#E0F2FE,stroke:#0284C7,stroke-width:2px,color:#0C4A6E;
    classDef model fill:#FEF3C7,stroke:#D97706,stroke-width:2px,color:#78350F;
    classDef ops fill:#DCFCE7,stroke:#16A34A,stroke-width:2px,color:#14532D;

    class U user;
    class A,I,P ui;
    class F,S feature;
    class D,R model;
    class N,REQ,DOCKER,CI ops;

    style UX fill:#F8FAFC,stroke:#94A3B8,stroke-width:1.5px;
    style FEAT fill:#EFF6FF,stroke:#60A5FA,stroke-width:1.5px;
    style ML fill:#FFFBEB,stroke:#F59E0B,stroke-width:1.5px;
    style OPS fill:#F0FDF4,stroke:#22C55E,stroke-width:1.5px;
```

This architecture captures the full lifecycle of the flight delay prediction system: the user submits flight inputs, the app prepares feature vectors using a schema, XGBoost models predict departure and arrival delays, and the project is trained, packaged, and automated through Docker and GitHub Actions.
