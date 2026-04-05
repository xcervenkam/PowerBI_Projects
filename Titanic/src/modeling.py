from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from .preprocessing import split_feature_types, make_preprocessor


RANDOM_STATE = 42
MASTER_NUMERIC_FEATURES = ["Age", "Fare", "FamilySize"]
MASTER_CATEGORICAL_FEATURES = ["Pclass", "Sex", "Embarked", "IsAlone", "Deck"]


def make_logreg_pipeline(features, C=1.0, penalty="l2", class_weight=None):
    numeric_features, categorical_features = split_feature_types(
        features,
        MASTER_NUMERIC_FEATURES,
        MASTER_CATEGORICAL_FEATURES
    )

    preprocessor = make_preprocessor(numeric_features, categorical_features)

    return Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(
            C=C,
            penalty=penalty,
            class_weight=class_weight,
            solver="liblinear",
            max_iter=1000,
            random_state=RANDOM_STATE
        ))
    ])


def make_rf_pipeline(features, **rf_params):
    numeric_features, categorical_features = split_feature_types(
        features,
        MASTER_NUMERIC_FEATURES,
        MASTER_CATEGORICAL_FEATURES
    )

    preprocessor = make_preprocessor(numeric_features, categorical_features)

    return Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestClassifier(
            random_state=RANDOM_STATE,
            **rf_params
        ))
    ])