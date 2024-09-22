# Definition des Parameter-Rasters
#   'n_estimators':  [50, 100, 200] [50, 200]
#   'max_depth': [None, 10, 20, 30] [None, 10]
#   'min_samples_split': [2, 5, 10] [2, 5]

param_grid = {
    'n_estimators': [50, 100, 200],  
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# GridSearchCV mit 5-facher Kreuzvalidierung
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1)

# Fitting des Modells mit den verschiedenen Hyperparameter-Kombinationen
grid_search.fit(X_train_scaled, y_train)

# Beste Parameter anzeigen
best_params = grid_search.best_params_
print(f'\nBeste Parameter: {best_params}')

# Modell mit den besten Parametern auf den Testdaten evaluieren
y_pred_best_rf = grid_search.best_estimator_.predict(X_test_scaled)

# Berechnung des Mean Squared Error (MSE) und des R²-Werts für das optimierte Modell
mse_best_rf = mean_squared_error(y_test, y_pred_best_rf)
r2_best_rf = r2_score(y_test, y_pred_best_rf)

# Ergebnisse anzeigen
print(f'\nOptimiertes Modell - Mean Squared Error: {mse_best_rf}')
print(f'Optimiertes Modell - R²-Wert: {r2_best_rf}')

# Feature-Importances und Vergleich mit tatsächlichen Werten (Summary)
feature_importances = grid_search.best_estimator_.feature_importances_
importance_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': feature_importances
}).sort_values(by='Importance', ascending=False)

# Anzeige der Feature-Wichtigkeit
print("\nFeature Importances:")
display(importance_df)

# Vergleich von Vorhersagen mit den tatsächlichen Werten
comparison_df = pd.DataFrame({
    'Tatsächliche Werte': y_test[:10],  # Die ersten 10 tatsächlichen Werte
    'Vorhersagen': y_pred_best_rf[:10]  # Die ersten 10 Vorhersagen
})

print("\nVergleich der ersten 10 Vorhersagen mit den tatsächlichen Werten:")
display(comparison_df)