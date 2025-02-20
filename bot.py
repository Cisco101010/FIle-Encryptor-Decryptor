from tradingview_ta import TA_Handler, Interval
import pandas as pd
import matplotlib.pyplot as plt

# Configuración del handler para ETH/USDT en Binance, temporalidad de 15 minutos
eth_handler = TA_Handler(
    symbol="ETHUSDT",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_15_MINUTES
)

# Obtener el análisis técnico
analysis = eth_handler.get_analysis()

# Extraer el precio actual
current_price = analysis.indicators.get("close")
print(f"Precio actual de ETH/USDT: {current_price}")

# Extraer indicadores específicos
rsi = analysis.indicators.get("RSI")
stoch_rsi_k = analysis.indicators.get("Stoch.RSI.K")  # RSI Estocástico K
volume = analysis.indicators.get("volume")
bb_upper = analysis.indicators.get("BB.upper")
bb_middle = analysis.indicators.get("SMA20")  # Banda media como SMA20
bb_lower = analysis.indicators.get("BB.lower")
macd = analysis.indicators.get("MACD.macd")
macd_signal = analysis.indicators.get("MACD.signal")
adx = analysis.indicators.get("ADX")
stoch_k = analysis.indicators.get("Stoch.K")  # Oscilador Estocástico K
stoch_d = analysis.indicators.get("Stoch.D")  # Oscilador Estocástico D
cci = analysis.indicators.get("CCI20")
ema50 = analysis.indicators.get("EMA50")
ema200 = analysis.indicators.get("EMA200")

# Extraer niveles de soporte y resistencia (método clásico)
support_1 = analysis.indicators.get("Pivot.M.Classic.S1")
support_2 = analysis.indicators.get("Pivot.M.Classic.S2")
resistance_1 = analysis.indicators.get("Pivot.M.Classic.R1")
resistance_2 = analysis.indicators.get("Pivot.M.Classic.R2")

# Mostrar valores
print(f"RSI: {rsi}")
print(f"RSI Estocástico (K): {stoch_rsi_k if stoch_rsi_k is not None else 'No disponible'}")
print(f"Volumen: {volume}")
print(f"Bandas de Bollinger - Superior: {bb_upper}, Media: {bb_middle if bb_middle is not None else 'No disponible'}, Inferior: {bb_lower}")
print(f"MACD: {macd}, Señal: {macd_signal}")
print(f"ADX: {adx}")
print(f"Oscilador Estocástico - K: {stoch_k}, D: {stoch_d}")
print(f"CCI: {cci}")
print(f"EMA50: {ema50}, EMA200: {ema200}")
print(f"Zona de Soporte 1: {support_1}, Soporte 2: {support_2}")
print(f"Zona de Resistencia 1: {resistance_1}, Resistencia 2: {resistance_2}")

# Resumen de la recomendación de TradingView
summary = analysis.summary
print(f"Recomendación: {summary['RECOMMENDATION']}")
print(f"Compra: {summary['BUY']}, Venta: {summary['SELL']}, Neutral: {summary['NEUTRAL']}")

# Diccionario de indicadores para visualización
indicators = {
    'RSI': rsi,
    'RSI Estocástico (K)': stoch_rsi_k if stoch_rsi_k is not None else 0,
    'Volumen': volume,
    'BB Superior': bb_upper,
    'BB Media': bb_middle if bb_middle is not None else current_price,
    'BB Inferior': bb_lower,
    'MACD': macd,
    'MACD Señal': macd_signal,
    'ADX': adx,
    'Stoch.K': stoch_k,
    'Stoch.D': stoch_d,
    'CCI': cci,
    'EMA50': ema50,
    'EMA200': ema200,
    'Precio Actual': current_price,
    'Soporte 1': support_1,
    'Soporte 2': support_2,
    'Resistencia 1': resistance_1,
    'Resistencia 2': resistance_2
}

# Crear un DataFrame para visualización
df_indicators = pd.DataFrame([indicators])

# Gráficos múltiples para mejor análisis
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico 1: RSI y RSI Estocástico
df_indicators[['RSI', 'RSI Estocástico (K)']].plot(kind='bar', ax=axs[0, 0])
axs[0, 0].axhline(70, color='red', linestyle='--', label='Sobrecompra (70)')
axs[0, 0].axhline(30, color='green', linestyle='--', label='Sobreventa (30)')
axs[0, 0].set_title('RSI y RSI Estocástico (K)')
axs[0, 0].set_ylabel('Valor')
axs[0, 0].legend()

# Gráfico 2: Oscilador Estocástico
df_indicators[['Stoch.K', 'Stoch.D']].plot(kind='bar', ax=axs[0, 1])
axs[0, 1].axhline(80, color='red', linestyle='--', label='Sobrecompra (80)')
axs[0, 1].axhline(20, color='green', linestyle='--', label='Sobreventa (20)')
axs[0, 1].set_title('Oscilador Estocástico (K y D)')
axs[0, 1].set_ylabel('Valor')
axs[0, 1].legend()

# Gráfico 3: MACD y Señal
df_indicators[['MACD', 'MACD Señal']].plot(kind='bar', ax=axs[1, 0])
axs[1, 0].set_title('MACD y Señal')
axs[1, 0].set_ylabel('Valor')
axs[1, 0].legend()

# Gráfico 4: Precio con Soportes y Resistencias
axs[1, 1].bar(['Precio Actual', 'Soporte 1', 'Soporte 2', 'Resistencia 1', 'Resistencia 2'], 
              [current_price, support_1, support_2, resistance_1, resistance_2], 
              color=['blue', 'green', 'darkgreen', 'red', 'darkred'])
axs[1, 1].set_title('Precio Actual con Soportes y Resistencias')
axs[1, 1].set_ylabel('Precio (USDT)')
axs[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()