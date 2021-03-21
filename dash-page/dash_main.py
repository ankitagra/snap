import dash
import dash_html_components as html
import dash_core_components as dcc
from style_common import colors, header_colors, pane_colors
from app_components import trade_params_pane, get_monte_carlo_pricer_pane, get_deep_learning_pricer_pane, \
    header_component, snap_description_component, header_top_component

import numpy as np
import scipy.stats as si
from tensorflow.keras.models import load_model

later_model = load_model(r'C:\Ankit\PythonProjects\hackathon\DeepLearning\300ksamples.h5', compile=False)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash('SNAP', external_stylesheets=external_stylesheets)

app.layout = html.Div(
    style={'backgroundColor': colors['background'], 'height': '100%'},
    children=[

        header_top_component,
        header_component,

        html.Br(),

        snap_description_component,

        html.Table(children=[
            html.Tr(children=[
                html.Td(trade_params_pane, style={'width': '28%'}),
                html.Td(get_monte_carlo_pricer_pane(app), style={'width': '35%'}),
                html.Td(get_deep_learning_pricer_pane(app), style={'width': '35%'}),
            ],
                # row-style
                style={})
        ],
            # table style
            style={'width': '98%'}),

    ],
)


@app.callback(
    dash.dependencies.Output('strike-output', 'children'),
    [dash.dependencies.Input('strike-input', 'drag_value')])
def update_output(value):
    return f'{value}'


@app.callback(
    dash.dependencies.Output('spot-output', 'children'),
    [dash.dependencies.Input('spot-input', 'drag_value')])
def update_output(value):
    return f'{value}'


@app.callback(
    dash.dependencies.Output('time-to-maturity-output', 'children'),
    [dash.dependencies.Input('time-to-maturity-input', 'drag_value'),
     dash.dependencies.Input('time-to-maturity-input', 'marks')]
)
def update_output(drag_value, marks):
    return f'{marks[str(drag_value)] if drag_value else "6m"}'


@app.callback(
    dash.dependencies.Output('risk-free-rate-output', 'children'),
    [dash.dependencies.Input('risk-free-rate-input', 'drag_value')])
def update_output(drag_value):
    return f'{drag_value}%'


# @app.callback(
#     dash.dependencies.Output('dividend-yield-output', 'children'),
#     [dash.dependencies.Input('dividend-yield-input', 'drag_value')])
# def update_output(drag_value):
#     return f'{drag_value}%'


@app.callback(
    dash.dependencies.Output('vol-output', 'children'),
    [dash.dependencies.Input('vol-input', 'drag_value')])
def update_output(drag_value):
    return f'{drag_value}%'


@app.callback(
    dash.dependencies.Output('monte-carlo-price-input', 'children'),
    [dash.dependencies.Input('strike-input', 'drag_value'),
     dash.dependencies.Input('spot-input', 'drag_value'),
     dash.dependencies.Input('time-to-maturity-input', 'marks'),
     dash.dependencies.Input('time-to-maturity-input', 'drag_value'),
     dash.dependencies.Input('risk-free-rate-input', 'drag_value'),
     dash.dependencies.Input('vol-input', 'drag_value'),
     ])
def update_output(strike, spot, time_to_maturity_marks, time_to_maturity_index, risk_free_rate, dividend_yield):
    import time
    ttm = time_to_maturity_marks[str(time_to_maturity_index) if time_to_maturity_index else '3']
    markdown = f'''
    ##### **Inputs**:
    * Strike: {strike}
    * Spot: {spot}
    * Time to Maturity: {ttm}
    * Risk Free Rate: {risk_free_rate}
    * Dividend Yield: {dividend_yield}    
    '''
    return markdown
    # return f'Price is {strike}, {spot}, {ttm}, {risk_free_rate}%, {dividend_yield}%'


@app.callback(
    dash.dependencies.Output('monte-carlo-price-output', 'children'),
    [dash.dependencies.Input('monte-carlo-submit-val', 'n_clicks'),
     dash.dependencies.State('strike-input', 'drag_value'),
     dash.dependencies.State('spot-input', 'drag_value'),
     dash.dependencies.State('time-to-maturity-input', 'marks'),
     dash.dependencies.State('time-to-maturity-input', 'drag_value'),
     dash.dependencies.State('risk-free-rate-input', 'drag_value'),
     dash.dependencies.State('vol-input', 'drag_value'),
     ])
def update_output(n_clicks, strike, spot, time_to_maturity_marks, time_to_maturity_index, risk_free_rate,
                  dividend_yield):
    import time
    start = time.time()
    time.sleep(3.5)
    ttm = time_to_maturity_marks[str(time_to_maturity_index) if time_to_maturity_index else '3']
    price = get_monte_carlo_price(strike=strike, spot=spot, ttm=ttm, rfr=risk_free_rate, vol=dividend_yield)
    time_taken = time.time() - start
    markdown = f'''
    ##### **Outputs**:
    ###### Price: {price}
    ###### Time taken: {time_taken:0.3f} s
    '''
    return markdown
    # markdown = f'''
    # Price: 3,
    # Time taken: {round(time.time() - start, 1)} secs
    # '''
    # return markdown
    # return f'Price is {strike}, {spot}, {ttm}, {risk_free_rate}%, {dividend_yield}%'


@app.callback(
    dash.dependencies.Output('deep-learning-price-input', 'children'),
    [dash.dependencies.Input('strike-input', 'drag_value'),
     dash.dependencies.Input('spot-input', 'drag_value'),
     dash.dependencies.Input('time-to-maturity-input', 'marks'),
     dash.dependencies.Input('time-to-maturity-input', 'drag_value'),
     dash.dependencies.Input('risk-free-rate-input', 'drag_value'),
     dash.dependencies.Input('vol-input', 'drag_value'),
     ])
def update_output(strike, spot, time_to_maturity_marks, time_to_maturity_index, risk_free_rate, dividend_yield):
    ttm = time_to_maturity_marks[str(time_to_maturity_index) if time_to_maturity_index else '3']
    markdown = f'''
    ##### **Inputs**:
    * Strike: {strike}
    * Spot: {spot}
    * Time to Maturity: {ttm}
    * Risk Free Rate: {risk_free_rate}
    * Dividend Yield: {dividend_yield}    
    '''
    return markdown
    # return f'Price is {strike}, {spot}, {ttm}, {risk_free_rate}%, {dividend_yield}%'


@app.callback(
    dash.dependencies.Output('deep-learning-price-output', 'children'),
    [dash.dependencies.Input('strike-input', 'drag_value'),
     dash.dependencies.Input('spot-input', 'drag_value'),
     dash.dependencies.Input('time-to-maturity-input', 'marks'),
     dash.dependencies.Input('time-to-maturity-input', 'drag_value'),
     dash.dependencies.Input('risk-free-rate-input', 'drag_value'),
     dash.dependencies.Input('vol-input', 'drag_value'),
     ])
def update_output(strike, spot, time_to_maturity_marks, time_to_maturity_index, risk_free_rate,
                  dividend_yield):
    # import time
    # start = time.time()
    ttm = time_to_maturity_marks[str(time_to_maturity_index) if time_to_maturity_index else '3']
    price, time_taken = get_deep_learning_price(strike=strike, spot=spot, ttm=ttm, rfr=risk_free_rate, vol=dividend_yield)
    markdown = f'''
    ##### **Outputs**:
    ###### Price: {price:0.3f}
    ###### Time taken: {time_taken:0.3f} s
    '''
    return markdown
    # markdown = f'''
    # Price: 3,
    # Time taken: {round(time.time() - start, 1)} secs
    # '''
    # return markdown
    # return f'Price is {strike}, {spot}, {ttm}, {risk_free_rate}%, {dividend_yield}%'


def get_monte_carlo_price(strike, spot, ttm, rfr, vol):
    if strike is None or spot is None or ttm is None or rfr is None or vol is None:
        return f'No inputs'
    else:
        strike_input = 1.0
        spot_input = spot / strike
        ttm_input = {'1m': 1 / 12.0, '3m': 0.25, '6m': 0.5, '1y': 1.0, '2y': 2.0}[ttm]
        rfr_input = rfr / 100.0
        div_yld_input = 0
        sigma = vol / 100.0
        pv = european_options(s=spot_input, k=strike_input, t=ttm_input, r=rfr_input - div_yld_input, sigma=sigma)
        # inputs = np.array([spot_input, strike_input, ttm_input, div_yld_input, 0.3, rfr_input])
        # inputs = inputs.reshape((1, 6))
        # pv = [0]
        # pv = later_model.predict(inputs)[0][0] * strike
        # return f'{strike}, {spot}, {ttm}, {rfr}%, {div_yld}%, 30%, {pv[0] * strike:0.4f}'
        return f'{pv[0] * strike:0.4f}'


def get_deep_learning_price(strike, spot, ttm, rfr, vol):
    if strike is None or spot is None or ttm is None or rfr is None or vol is None:
        return 0, 0
    else:
        strike_input = 1.0
        spot_input = spot / strike
        ttm_input = {'1m': 1 / 12.0, '3m': 0.25, '6m': 0.5, '1y': 1.0, '2y': 2.0}[ttm]
        rfr_input = rfr / 100.0
        div_yld_input = 0
        sigma = vol / 100.0
        inputs = np.array([spot_input, strike_input, ttm_input, div_yld_input, sigma, rfr_input])
        inputs = inputs.reshape((1, 6))
        # pv = [0]
        import time
        start = time.time()
        pv = later_model.predict(inputs)[0][0] * strike
        time_taken = time.time() - start
        return pv, time_taken
        # return f'{strike}, {spot}, {ttm}, {rfr}%, {div_yld}%, 30%, {pv:0.4f}'


def european_options(s, k, t, r, sigma):
    d1 = (np.log(s / k) + (r + (sigma ** 2 / 2) * t)) / (sigma * (np.sqrt(t)))
    d2 = d1 - sigma * (np.sqrt(t))

    call = s * si.norm.cdf(d1, 0, 1) - k * np.exp(-1.0 * r * t) * si.norm.cdf(d2)
    put = k * np.exp(-1.0 * r * t) * si.norm.cdf(-d2, 0, 1) - s * si.norm.cdf(-d1, 0, 1)
    # print (d1)
    return call, put
    # return call


# @app.callback(
#     dash.dependencies.Output('monte-carlo-price-output', 'children'),
#     [dash.dependencies.Input('strike-input', 'drag_value'),
#      dash.dependencies.Input('spot-input', 'drag_value'),
#      dash.dependencies.Input('time-to-maturity-input', 'marks'),
#      dash.dependencies.Input('time-to-maturity-input', 'drag_value'),
#      dash.dependencies.Input('risk-free-rate-input', 'drag_value'),
#      dash.dependencies.Input('dividend-yield-input', 'drag_value'),
#      ])
# def update_output(strike, spot, time_to_maturity_marks, time_to_maturity_index, risk_free_rate, dividend_yield):
#     import time
#     start = time.time()
#     time.sleep(2)
#     ttm = time_to_maturity_marks[str(time_to_maturity_index) if time_to_maturity_index else '3']
#     markdown = f'''
#     ##### **Outputs**:
#     ###### Price: {strike}, {spot}, {ttm}, {risk_free_rate}%, {dividend_yield}%
#     ###### Time taken: {round(time.time() - start, 1)} secs
#     '''
#     return markdown
#     # markdown = f'''
#     # Price: 3,
#     # Time taken: {round(time.time() - start, 1)} secs
#     # '''
#     # return markdown
#     # return f'Price is {strike}, {spot}, {ttm}, {risk_free_rate}%, {dividend_yield}%'


# @app.callback(
#     dash.dependencies.Output('deep-learning-price-output', 'children'),
#     [dash.dependencies.Input('strike-input', 'drag_value'),
#      dash.dependencies.Input('spot-input', 'drag_value'),
#      dash.dependencies.Input('time-to-maturity-input', 'marks'),
#      dash.dependencies.Input('time-to-maturity-input', 'drag_value'),
#      dash.dependencies.Input('risk-free-rate-input', 'drag_value'),
#      dash.dependencies.Input('dividend-yield-input', 'drag_value'),
#      ])
# def update_output(strike, spot, time_to_maturity_marks, time_to_maturity_index, risk_free_rate, dividend_yield):
#     ttm = time_to_maturity_marks[str(time_to_maturity_index) if time_to_maturity_index else '3']
#     return f'Price is {strike}, {spot}, {ttm}, {risk_free_rate}%, {dividend_yield}%'


# @app.callback(
#     dash.dependencies.Output('container-button-dl', 'children'),
#     [dash.dependencies.Input('submit-val-dl', 'n_clicks')],
#     [dash.dependencies.State('input-on-submit', 'value')])
# def update_output(n_clicks, value):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         n_clicks
#     )
#
#
# @app.callback(
#     dash.dependencies.Output('container-button-mc', 'children'),
#     [dash.dependencies.Input('submit-val-mc', 'n_clicks')],
#     [dash.dependencies.State('input-on-submit', 'value')])
# def update_output(n_clicks, value):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         n_clicks
#     )


if __name__ == '__main__':
    app.run_server(debug=True)
