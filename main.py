# Import necessary libraries and modules
import numpy as np


import streamlit as st

condition_and_maintenance = {
    'inspection_report': 'Good condition with recent maintenance.',
    'maintenance_history': 'Regular maintenance and no major repairs.'
}

market_data = {
    'current_market_conditions': 'Stable with moderate demand for container ships.',
    'historical_sales_data': [75000000, 70000000, 72000000, 68000000, 71000000],
    'market_trends': 'Container shipping rates have been steady.'
}

geographic_location = {
    'location': 'Port of Los Angeles, USA'
}

economic_factors = {
    'economic_indicators': 'Stable economy with low inflation and interest rates.'
}

regulatory_compliance = {
    'compliance_status': 'Fully compliant with international regulations.'
}

special_features = {
    'advanced_navigational_system': True,
    'eco_friendly_equipment': False
}

ownership_history = {
    'previous_owners': ['ABC Shipping Co.', 'XYZ Maritime Ltd.'],
    'notable_events': 'No major incidents in the ship’s history.'
}

# Define valuation methodology and weights
valuation_weights = {
    'age_weight': 0.001,
    'size_weight': 0.001,
    'condition_weight': 0.001,
    'market_data_weight': 0.0015,
    'location_weight': 0.005,
    'economic_factors_weight': 0.005,
    'compliance_weight': 0.005,
    'special_features_weight': 0.001,
    'ownership_history_weight': 0.001,
    'risk_assessment_weight': 0.001,
    'discount_rate': 0.008  # Used for discounted cash flow (DCF) valuation
}


# Define valuation algorithm
def value_ship(ship_characteristics, condition_and_maintenance, market_data,
               geographic_location, economic_factors, regulatory_compliance,
               special_features, ownership_history, valuation_weights):
    """
    Estimate the value of a ship based on various factors and weights.
    """

    # Age-based valuation (linear depreciation)
    age_valuation = (1 - (ship_characteristics['age_years'] / 30)) * valuation_weights['age_weight']

    # Size-based valuation
    size_factor = {
        'Container Ship': 0.08,
        'Tanker': 0.1,
        'Bulk Carrier': 0.07,
        'Fishing Vessel': 0.05
    }
    size_valuation = (ship_characteristics['gross_tonnage'] / 100000) * size_factor.get(
        ship_characteristics['ship_type'], 0) * valuation_weights['size_weight']

    # Condition-based valuation
    condition_valuation = {
                              'Excellent': 0.1,
                              'Good': 0.07,
                              'Fair': 0.03,
                              'Poor': 0.01
                          }.get(condition_and_maintenance['inspection_report'], 0) * valuation_weights[
                              'condition_weight']

    # Market data-based valuation (DCF)
    avg_annual_cash_flow = market_data['historical_sales_data'][0] * 0.1  # Assume 10% of the initial sale price
    dcf_valuation = (avg_annual_cash_flow / (1 + valuation_weights['discount_rate']) ** ship_characteristics[
        'age_years']) * valuation_weights['market_data_weight']

    # Location-based valuation
    location_factor = {
        'Port of Los Angeles, USA': 1.05,
        'Singapore Port': 1.03,
        'Rotterdam Port': 1.02,
        'Other': 1.0
    }
    location_valuation = location_factor.get(geographic_location['location'], 1.0) * valuation_weights[
        'location_weight']

    # Economic factors-based valuation
    economic_valuation = {
                             'Stable': 0.1,
                             'Moderate': 0.05,
                             'Unstable': 0.02
                         }.get(economic_factors['economic_indicators'], 0) * valuation_weights[
                             'economic_factors_weight']

    # Compliance-based valuation
    compliance_valuation = {
                               'Fully compliant with international regulations.': 0.1,
                               'Partial compliance with minor issues.': 0.05,
                               'Non-compliant with significant issues.': 0.02
                           }.get(regulatory_compliance['compliance_status'], 0) * valuation_weights['compliance_weight']

    # Special features-based valuation
    special_features_valuation = (int(special_features['advanced_navigational_system']) * 0.03 +
                                  int(special_features['eco_friendly_equipment']) * 0.02) * valuation_weights[
                                     'special_features_weight']

    # Ownership history-based valuation
    ownership_valuation = len(ownership_history['previous_owners']) * 0.01 * valuation_weights[
        'ownership_history_weight']

    # Calculate the total estimated value
    estimated_value = (age_valuation + size_valuation + condition_valuation +
                       dcf_valuation + location_valuation + economic_valuation +
                       compliance_valuation + special_features_valuation +
                       ownership_valuation) * np.mean(market_data['historical_sales_data'])

    return estimated_value




#print(f"The estimated value of the ship is: ${estimated_value:,.2f}")

# Define Streamlit app
def main():
    st.title('Ship Valuation App')

    # Input widgets for ship_characteristics
    st.sidebar.header('Ship Characteristics Input')
    ship_type = st.sidebar.selectbox('Ship Type', ['Container Ship', 'Tanker', 'Bulk Carrier', 'Fishing Vessel'])
    age_years = st.sidebar.number_input('Age (years)', value=10, min_value=1, step=1)
    length = st.sidebar.number_input('Length (meters)', value=200, min_value=1, step=1)
    width = st.sidebar.number_input('Width (meters)', value=30, min_value=1, step=1)
    draft = st.sidebar.number_input('Draft (meters)', value=12, min_value=1, step=1)
    gross_tonnage = st.sidebar.number_input('Gross Tonnage', value=50000, min_value=1, step=1)
    engine_power_hp = st.sidebar.number_input('Engine Power (HP)', value=40000, min_value=1, step=1)
    cargo_capacity_tons = st.sidebar.number_input('Cargo Capacity (tons)', value=25000, min_value=1, step=1)

    # Assigning inputs to ship_characteristics dictionary
    ship_characteristics = {
        'ship_type': ship_type,
        'age_years': age_years,
        'size_meters': {'length': length, 'width': width, 'draft': draft},
        'gross_tonnage': gross_tonnage,
        'engine_power_hp': engine_power_hp,
        'cargo_capacity_tons': cargo_capacity_tons
    }


    if st.button('Calculate Valuation'):
        ship_valuation = value_ship(ship_characteristics, condition_and_maintenance, market_data,
                             geographic_location, economic_factors, regulatory_compliance,
                             special_features, ownership_history, valuation_weights)
        st.success(f"The estimated value of the ship is ${ship_valuation:,.2f}.")


if __name__ == "__main__":
    main()