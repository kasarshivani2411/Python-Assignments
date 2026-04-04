import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    # ---------------------------------------------------------------
    # Step 1 : Load Dataset
    # ---------------------------------------------------------------
    print("\nStep 1 : Load Dataset")

    df = pd.read_csv("student-mat.csv", sep=';')   # important: ; separator

    print("\nFirst few records:")
    print(df.head())

    print("\nShape of dataset:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    # ---------------------------------------------------------------
    # Step 2 : Select Features
    # ---------------------------------------------------------------
    print("\nStep 2 : Select Features")

    X = df[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    print("\nSelected features:")
    print(X.head())

    print("\nShape of selected features:")
    print(X.shape)

    # ---------------------------------------------------------------
    # Step 3 : Scale Data
    # ---------------------------------------------------------------
    print("\nStep 3 : Scale Data")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("\nScaled data (first 5 rows):")
    print(X_scaled[:5])

    # ---------------------------------------------------------------
    # Step 4 : Elbow Method
    # ---------------------------------------------------------------
    print("\nStep 4 : Elbow Method")

    WCSS = []

    for i in range(1, 11):
        model = KMeans(n_clusters=i, random_state=42, n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), WCSS, marker='o')
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.grid(True)
    plt.show()

    # ---------------------------------------------------------------
    # Step 5 : Train Model (k = 3)
    # ---------------------------------------------------------------
    print("\nStep 5 : Train Model")

    model = KMeans(n_clusters=3, random_state=42, n_init=10)

    clusters = model.fit_predict(X_scaled)
    df["Cluster"] = clusters

    print("\nDataset with clusters:")
    print(df[["G1","G2","G3","studytime","failures","absences","Cluster"]].head(20))

    # ---------------------------------------------------------------
    # Step 6 : Cluster Analysis
    # ---------------------------------------------------------------
    print("\nStep 6 : Cluster Analysis (Mean Values)")

    cluster_summary = df.groupby("Cluster")[["G1","G2","G3","studytime","failures","absences"]].mean()
    print(cluster_summary)

    # ---------------------------------------------------------------
    # Step 7 : Visualization
    # ---------------------------------------------------------------
    print("\nStep 7 : Visualization")

    plt.figure(figsize=(8,6))
    plt.scatter(df["G3"], df["absences"], c=df["Cluster"], cmap='viridis')
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Absences")
    plt.title("Student Clusters")
    plt.colorbar(label="Cluster")
    plt.show()

if __name__ == "__main__":
    main()