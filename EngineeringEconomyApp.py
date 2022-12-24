import streamlit as st

hide_menu = """
<style>
#MainMenu{
    Visibility:hidden;
}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

hide_share = """
<style>
#Share{
    Visibility:hidden;
}
</style>
"""
st.markdown(hide_share, unsafe_allow_html=True)

hide_star = """
<style>
#stActionButton{
    Visibility:hidden;
}
</style>
"""
st.markdown(hide_star, unsafe_allow_html=True)

st.sidebar.image('logo_kent.png')
st.sidebar.markdown("""
            <h1 class = title1>
                Kent Katigbak
            </h1>
            <h3 class = subtitle1>
            Industrial Engineer, CLSSYB, SO2, PMFC, CIFC, DSFC, Data Analyst, Python Programmer
            </h3>
            <style>
                .title1 {
                padding-bottom: 0rem;
            }
                .subtitle1 {
                padding-top: 0rem;
                padding-right: 0rem;
                padding-bottom: 3.5rem;
            }
    </style>
    """, unsafe_allow_html=True)

st.title("Engineering Economy Web App")

# Menu
app_menu = st.selectbox(
    "Choose what to calculate:",
    ("Simple Interest", "Compound Interest", "Annuity", "Capitalized Cost", "Annual Cost", "Depreciation",
    "Depletion", "Capital Recovery", "Property Valuation or Appraisal", "Principles of Accounting", "Cost Accounting",
    "Break-Even Analysis", "Minimum Cost Analysis", "Public Economy", "Inflation", "Deflation", "Risk and Uncertainty")
    )

# Simple Interest
if app_menu == "Simple Interest":
    st.title("Simple Interest Calculator")

    # display definition and formula of simple interest
    st.write("Simple interest is the interest paid on the principal amount only. It is calculated using the formula:")
    st.write("Simple Interest = Principal x Rate x Time / 100")

    # create sidebar for input options
    st.subheader("Input necessary values")
    principal = st.number_input("Principal")
    rate = st.number_input("Rate (%)")
    time = st.number_input("Time (years)")

    # calculate and display simple interest
    simple_interest = principal * rate * time / 100
    st.write(f"Simple Interest: {simple_interest}")

# Compound Interest
if app_menu == "Compound Interest":
    st.title("Compound Interest Calculator")

    # display definition and formula of compound interest
    st.write("Compound interest is the interest paid on the initial principal and on the accumulated interest of previous periods. It is calculated using the formula:")
    st.write("Compound Interest = Principal x (1 + Rate / 100)^Time")

    # create sidebar for input options
    st.subheader("Input necessary values")
    principal = st.number_input("Principal")
    rate = st.number_input("Rate (%)")
    time = st.number_input("Time (years)")

    # calculate and display compound interest
    compound_interest = principal * (1 + rate / 100)**time
    st.write(f"Compound Interest: {compound_interest}")

# Annuity
if app_menu == "Annuity":
    from scipy.optimize import fsolve

    st.title("Annuity Calculator")

    # display definition and formula of annuity
    st.write("An annuity is a series of equal periodic payments or receipts that occur at regular intervals. It is calculated using the formula:")
    st.write("Annuity = Payment / Interest Rate")

    # create sidebar for input options
    st.subheader("Input necessary values")
    payment = st.number_input("Payment")
    rate = st.number_input("Interest Rate (%)")

    # calculate and display annuity
    def func(x):
        return payment - x * (1 - (1 + rate/100)**(-12)) / (rate/100)
    annuity, = fsolve(func, 0)
    st.write(f"Annuity: {annuity}")

# Capitalized Cost
if app_menu == "Capitalized Cost":
    st.title("Capitalized Cost Calculator")

    # display definition and formula of capitalized cost
    st.write("Capitalized cost is the total cost of an asset including its purchase price, installation costs, and any other expenses incurred in acquiring and preparing it for use. It is calculated using the formula:")
    st.write("Capitalized Cost = Purchase Price + Installation Costs + Other Expenses")

    # create sidebar for input options
    st.subheader("Input necessary values")
    purchase_price = st.number_input("Purchase Price")
    installation_costs = st.number_input("Installation Costs")
    other_expenses = st.number_input("Other Expenses")

    # calculate and display capitalized cost
    capitalized_cost = purchase_price + installation_costs + other_expenses
    st.write(f"Capitalized Cost: {capitalized_cost}")

# Annual Cost
if app_menu == "Annual Cost":
    st.title("Annual Cost Calculator")

    # display definition and formula of annual cost
    st.write("Annual cost is the total cost of an asset or service over a one-year period. It is calculated using the formula:")
    st.write("Annual Cost = Capitalized Cost / Useful Life")

    # create sidebar for input options
    st.subheader("Input necessary values")
    capitalized_cost = st.number_input("Capitalized Cost")
    useful_life = st.number_input("Useful Life (years)")

    # calculate and display annual cost
    annual_cost = capitalized_cost / useful_life
    st.write(f"Annual Cost: {annual_cost}")

# Depreciation
if app_menu == "Depreciation":
    st.title("Depreciation Calculator")

    # display definition and formula of depreciation
    st.write("Depreciation is the allocation of the cost of an asset over its useful life. It is calculated using the formula:")
    st.write("Depreciation = (Capitalized Cost - Salvage Value) / Useful Life")

    # create sidebar for input options
    st.subheader("Input necessary values")
    capitalized_cost = st.number_input("Capitalized Cost")
    salvage_value = st.number_input("Salvage Value")
    useful_life = st.number_input("Useful Life (years)")

    # calculate and display depreciation
    depreciation = (capitalized_cost - salvage_value) / useful_life
    st.write(f"Depreciation: {depreciation}")

# Depletion
if app_menu == "Depletion":
    st.title("Depletion Calculator")

    # display definition and formula of depletion
    st.write("Depletion is the process of consuming a resource, such as a natural resource, by using it or extracting it. It is calculated using the formula:")
    st.write("Depletion = (Original Quantity - Remaining Quantity) / Total Production")

    # create sidebar for input options
    st.subheader("Input necessary values")
    original_quantity = st.number_input("Original Quantity")
    remaining_quantity = st.number_input("Remaining Quantity")
    total_production = st.number_input("Total Production")

    # calculate and display depletion
    depletion = (original_quantity - remaining_quantity) / total_production
    st.write(f"Depletion: {depletion}")

# Capital Recovery
if app_menu == "Capital Recovery":
    st.title("Capital Recovery Calculator")

    # display definition and formula of capital recovery
    st.write("Capital recovery is the process of recovering the original investment in an asset over a specified period of time. It is calculated using the formula:")
    st.write("Capital Recovery = Investment / Annual Return")

    # create sidebar for input options
    st.subheader("Input necessary values")
    investment = st.number_input("Investment")
    annual_return = st.number_input("Annual Return")

    # calculate and display capital recovery
    capital_recovery = investment / annual_return
    st.write(f"Capital Recovery: {capital_recovery}")

# Property Valuation or Appraisal
if app_menu == "Property Valuation or Appraisal":
    st.title("Property Valuation Calculator")

    # display definition and formula of property valuation or appraisal
    st.write("Property valuation or appraisal is the process of estimating the market value of a property. It is calculated using the formula:")
    st.write("Property Valuation = Market Value of Comparable Properties / Number of Comparable Properties")

    # create sidebar for input options
    st.subheader("Input necessary values")
    market_value = st.number_input("Market Value of Comparable Properties")
    number_of_properties = st.number_input("Number of Comparable Properties")

    # calculate and display property valuation or appraisal
    property_valuation = market_value / number_of_properties
    st.write(f"Property Valuation: {property_valuation}")

# Principles of Accounting
if app_menu == "Principles of Accounting":
    st.title("Accounting Calculator")

    # display definition and principles of accounting
    st.write("Accounting is the process of recording, classifying, and summarizing financial transactions to provide information that is useful in making business decisions. The principles of accounting are the fundamental assumptions and guidelines that underlie the preparation of financial statements.")

    # create sidebar for input options
    st.subheader("Input necessary values")
    revenue = st.number_input("Revenue")
    cost_of_goods_sold = st.number_input("Cost of Goods Sold")
    expenses = st.number_input("Expenses")

    # calculate and display net income using the matching principle
    net_income = revenue - cost_of_goods_sold - expenses
    st.write(f"Net Income: {net_income}")

# Cost Accounting
if app_menu == "Cost Accounting":
    st.title("Cost Accounting Calculator")

    # display definition and principles of cost accounting
    st.write("Cost accounting is the process of recording, classifying, and summarizing costs to provide information that is useful in making business decisions. The principles of cost accounting are the fundamental assumptions and guidelines that underlie the preparation of cost statements.")

    # create sidebar for input options
    st.subheader("Input necessary values")
    direct_materials = st.number_input("Direct Materials")
    direct_labor = st.number_input("Direct Labor")
    factory_overhead = st.number_input("Factory Overhead")

    # calculate and display prime cost
    prime_cost = direct_materials + direct_labor
    st.write(f"Prime Cost: {prime_cost}")

    # calculate and display total manufacturing cost
    total_manufacturing_cost = prime_cost + factory_overhead
    st.write(f"Total Manufacturing Cost: {total_manufacturing_cost}")

# Break-Even Analysis
if app_menu == "Break-Even Analysis":
    st.title("Break Even Analysis Calculator")

    # display definition and formula of break even analysis
    st.write("Break even analysis is the process of calculating the number of units that must be sold to cover costs. It is calculated using the formula:")
    st.write("Break Even Point = Fixed Costs / (Price - Variable Costs)")

    # create sidebar for input options
    st.subheader("Input necessary values")
    fixed_costs = st.number_input("Fixed Costs")
    price = st.number_input("Price")
    variable_costs = st.number_input("Variable Costs")

    # calculate and display break even point
    break_even_point = fixed_costs / (price - variable_costs)
    st.write(f"Break Even Point: {break_even_point}")

# Minimum Cost Analysis
if app_menu == "Minimum Cost Analysis":
    st.title("Minimum Cost Analysis Calculator")

    # display definition and formula of minimum cost analysis
    st.write("Minimum cost analysis is the process of determining the lowest cost that can be incurred to achieve a specific goal. It is calculated using the formula:")
    st.write("Minimum Cost = Minimum Total Variable Costs + Minimum Fixed Costs")

    # create sidebar for input options
    st.subheader("Input necessary values")
    minimum_total_variable_costs = st.number_input("Minimum Total Variable Costs")
    minimum_fixed_costs = st.number_input("Minimum Fixed Costs")

    # calculate and display minimum cost
    minimum_cost = minimum_total_variable_costs + minimum_fixed_costs
    st.write(f"Minimum Cost: {minimum_cost}")

# Public Economy
if app_menu == "Public Economy":
    st.title("Public Economy Calculator")

    # display definition and principles of public economy
    st.write("Public economy is the branch of economics that studies the economic activity of the government and its impact on society. The principles of public economy include:")
    st.write("- The principle of efficiency: maximizing social welfare by minimizing costs and maximizing benefits")
    st.write("- The principle of equity: ensuring that the benefits and costs of economic activity are distributed fairly among individuals and groups in society")

    # create sidebar for input options
    st.subheader("Input necessary values")
    total_revenue = st.number_input("Total Revenue")
    total_expenditure = st.number_input("Total Expenditure")

    # calculate and display net fiscal position
    net_fiscal_position = total_revenue - total_expenditure
    st.write(f"Net Fiscal Position: {net_fiscal_position}")

    # calculate and display net public debt
    net_public_debt = net_fiscal_position * -1
    st.write(f"Net Public Debt: {net_public_debt}")

# Inflation
if app_menu == "Inflation":
    st.title("Inflation Calculator")

    # display definition and formula of inflation
    st.write("Inflation is the rate at which the general level of prices for goods and services is rising, and subsequently, purchasing power is falling. It is calculated using the formula:")
    st.write("Inflation = (Price in Current Period - Price in Previous Period) / Price in Previous Period")

    # create sidebar for input options
    st.subheader("Input necessary values")
    price_current_period = st.number_input("Price in Current Period")
    price_previous_period = st.number_input("Price in Previous Period")

    # calculate and display inflation
    inflation = (price_current_period - price_previous_period) / price_previous_period
    st.write(f"Inflation: {inflation}")

# Deflation
if app_menu == "Deflation":
    st.title("Deflation Calculator")

    # display definition and formula of deflation
    st.write("Deflation is the rate at which the general level of prices for goods and services is falling, and subsequently, purchasing power is rising. It is calculated using the formula:")
    st.write("Deflation = (Price in Previous Period - Price in Current Period) / Price in Previous Period")

    # create sidebar for input options
    st.subheader("Input necessary values")
    price_current_period = st.number_input("Price in Current Period")
    price_previous_period = st.number_input("Price in Previous Period")

    # calculate and display deflation
    deflation = (price_previous_period - price_current_period) / price_previous_period
    st.write(f"Deflation: {deflation}")

# Risk and Uncertainty
if app_menu == "Risk and Uncertainty":
    st.title("Risk and Uncertainty Calculator")

    # display definition and principles of risk and uncertainty
    st.write("Risk and uncertainty are two closely related concepts in economics. Risk is the likelihood that a certain event will occur, while uncertainty is the lack of information or knowledge about a certain event. The principles of risk and uncertainty include:")
    st.write("- The principle of diversification: reducing risk by investing in a variety of assets")
    st.write("- The principle of expected value: using probabilities to calculate the average outcome of a risky decision")

    # create sidebar for input options
    st.subheader("Input necessary values")
    probability = st.number_input("Probability")
    outcome1 = st.number_input("Outcome 1")
    outcome2 = st.number_input("Outcome 2")

    # calculate and display expected value
    expected_value = probability * outcome1 + (1 - probability) * outcome2
    st.write(f"Expected Value: {expected_value}")
