import dash_html_components as html
import dash_core_components as dcc
from style_common import colors, pane_colors, header_colors, output_colors

# Strike
# strike_component = html.Div(
#     children=[
#         html.Label('Strike', style={'font-size': 20}),
#         dcc.Slider(id='strike-input',
#                    min=60,
#                    max=140,
#                    value=100,
#                    marks={60: '60',
#                           80: '80',
#                           100: '100',
#                           120: '120',
#                           140: '140',
#                           }),
#         html.Div(id='strike-output', style={'textAlign': 'Right'}),
#         # dcc.Input(id='strike-input', type='text', value=100.0, style={'width': '90%'}),
#         # html.Label('Enter strike'),
#     ],
#     style={
#         'color': colors['text'],
#     }
# )


# Strike Label
strike_row11 = html.Td(children=[html.Label('Strike')],
                       style={
                           'font-size': 20,
                           'textAlign': 'left',
                           'width': '80%',
                           'border': 'None',
                       })

# Strike dummy
strike_row12 = html.Td(children=[html.Div('')],
                       style={
                           'width': '20%',
                           'border': 'None',
                       }
                       )

# Strike slider
strike_row21 = html.Td(children=[dcc.Slider(id='strike-input',
                                            min=90,
                                            max=110,
                                            value=100,
                                            marks={90: '90',
                                                   95: '95',
                                                   100: '100',
                                                   105: '105',
                                                   110: '110',
                                                   }),
                                 ],
                       style={
                           'width': '100%',
                           'textAlign': 'center',
                           'border': 'None',
                       }
                       )

# Strike output
strike_row22 = html.Td(children=[html.Div(id='strike-output')],
                       style={
                           'width': '20%',
                           'background-color': output_colors['background'],
                           'font-size': 20,
                           'textAlign': 'center',
                           'border': 'None',
                           'margin-right': '50px'
                       })

strike_component = html.Div(children=[
    html.Table(children=[
        html.Tr(children=[strike_row11, strike_row12], style={'width': '100%'}),
        html.Tr(children=[strike_row21, strike_row22], style={'width': '100%'})
    ],
        # table style
        style={'margin': '20px'}
    )
])

# strike_component = html.Div(children=[
#     html.Table(children=[
#         html.Tr(children=[strike_row11, strike_row12], style={'width': '100%'}),
#     ],
#         # table style
#         style={'margin': '10px'}
#     ),
#
#     html.Table(children=[
#         html.Tr(children=[strike_row21, strike_row22], style={'width': '100%'})
#     ],
#         # table style
#         style={'margin': '10px'}
#     ),
#
# ])

# # Implemented as Div -> Table -> 2 rows [Row1 - Label, Row2 - Slider+ChosenValue]
# strike_component = html.Div(
#     children=[
#
#         # Table of 2 rows - Label, Slider+ChosenValue
#         html.Table(children=[
#
#             # first row - Td(Label), Td(EmptyDiv)
#             html.Tr(children=[
#                 html.Td(children=[html.Label('Strike')],
#                         style={
#                             'font-size': 20,
#                             'textAlign': 'left',
#                             'width': '100%',
#                             'border': 'None',
#                         }
#                         ),
#                 html.Td(children=[html.Div('')],
#                         style={
#                             'width': '20%',
#                             'border': 'None',
#                         }
#                         ),
#             ],
#                 style={
#                     'width': '100%',
#                 }
#             ),
#
#             # second row - Td(slider), Td(ChosenValue)
#             html.Tr(children=[
#
#                 # slider
#                 html.Td(children=[dcc.Slider(id='strike-input',
#                                              min=60,
#                                              max=140,
#                                              value=100,
#                                              marks={60: '60',
#                                                     80: '80',
#                                                     100: '100',
#                                                     120: '120',
#                                                     140: '140',
#                                                     }),
#                                   ],
#                         style={
#                             'width': '80%',
#                             'textAlign': 'center',
#                             'border': 'None',
#                         }
#                         ),
#
#                 # ChosenValue
#                 html.Td(children=[html.Div(id='strike-output')],
#                         style={
#                             'width': '20%',
#                             'background-color': output_colors['background'],
#                             'textAlign': 'center',
#                             'border': 'None',
#                         }),
#             ],
#                 # second-row style
#                 style={
#                     'width': '100%',
#                     'border': 'None',
#                     # 'textAlign': 'center'
#                 }
#             ),  # second-row end
#
#         ],
#             # table-style
#             style={
#                 # 'border': '1px solid white',
#                 'color': colors['text'],
#                 # 'border-collapse': 'collapse',
#                 'margin': '10px',
#             }
#         ),  # table-end
#     ],  # div-children end
#
#     # div-style
#     style={
#         'color': colors['text'],
#     }
# )

# Spot
# spot_component = html.Div(
#     children=[
#         html.Label('Spot', style={'textAlign': 'Center', 'font-size': 20}),
#         dcc.Slider(id='spot-input',
#                    min=60,
#                    max=140,
#                    value=100,
#                    marks={60: '60',
#                           80: '80',
#                           100: '100',
#                           120: '120',
#                           140: '140',
#                           }),
#         html.Div(id='spot-output', style={'textAlign': 'Center'}),
#         # dcc.Input(id='spot-input', type='text', value=100.0, style={'width': '90%'}),
#         # html.Label('Enter strike'),
#     ],
#     style={
#         'color': colors['text'],
#     }
# )

# Spot Label
spot_row11 = html.Td(children=[html.Label('Spot')],
                     style={
                         'font-size': 20,
                         'textAlign': 'left',
                         'width': '80%',
                         'border': 'None',
                     })

# Spot dummy
spot_row12 = html.Td(children=[html.Div('')],
                     style={
                         'width': '20%',
                         'border': 'None',
                     }
                     )

# Spot slider
spot_row21 = html.Td(children=[dcc.Slider(id='spot-input',
                                          min=90,
                                          max=110,
                                          value=100,
                                          marks={90: '90',
                                                 95: '95',
                                                 100: '100',
                                                 105: '105',
                                                 110: '110',
                                                 }),
                               ],
                     style={
                         'width': '100%',
                         'textAlign': 'center',
                         'border': 'None',
                     }
                     )

# Spot output
spot_row22 = html.Td(children=[html.Div(id='spot-output')],
                     style={
                         'width': '20%',
                         'background-color': output_colors['background'],
                         'font-size': 20,
                         'textAlign': 'center',
                         'border': 'None',
                         'margin-right': '50px'
                     })

spot_component = html.Div(children=[
    html.Table(children=[
        html.Tr(children=[spot_row11, spot_row12], style={'width': '100%'}),
        html.Tr(children=[spot_row21, spot_row22], style={'width': '100%'})
    ],
        # table style
        style={'margin': '20px'}
    )
])

# Implemented as Div -> Table -> 2 rows [Row1 - Label, Row2 - Slider+ChosenValue]
# spot_component = html.Div(
#     children=[
#
#         # Table of 2 rows - Label, Slider+ChosenValue
#         html.Table(children=[
#
#             # first row - Label
#             html.Tr(children=[
#                 html.Label('Spot', style={'font-size': 20}),
#             ]),
#
#             # second row - slider + ChosenValue
#             html.Tr(children=[
#
#                 # slider
#                 html.Td(children=[
#                     dcc.Slider(id='spot-input',
#                                min=60,
#                                max=140,
#                                value=100,
#                                marks={60: '60',
#                                       80: '80',
#                                       100: '100',
#                                       120: '120',
#                                       140: '140',
#                                       }),
#                 ],
#                     style={
#                         'width': '100%',
#                         'border': 'None',
#                     }),
#
#                 # ChosenValue
#                 html.Td(children=[
#                     html.Div(id='spot-output', style={'textAlign': 'Right'}),
#                 ],
#                     # second-row style
#                     style={
#                         'border': 'None',
#                         'width': '100%'
#                     }),
#             ]),  # second-row end
#
#         ],
#             # table-style
#             style={
#                 'border': 'None',
#                 'color': colors['text'],
#             }
#         ),  # table-end
#     ],  # div-children end
#
#     # div-style
#     style={
#         'color': colors['text'],
#     }
# )

# Time to maturity
# time_to_maturity_component = html.Div(
#     children=[
#         html.Label('Time to Maturity', style={'textAlign': 'Center', 'font-size': 20}),
#         dcc.Slider(id='time-to-maturity-input',
#                    min=1,
#                    max=5,
#                    value=3,
#                    marks={1: '1m', 2: '3m', 3: '6m', 4: '1y', 5: '2y'}
#                    ),
#         html.Div(id='time-to-maturity-output', style={'textAlign': 'Center'}),
#         # dcc.Input(id='time-to-maturity-input', type='text', value=0.25, style={'width': '90%'}),
#         # html.Label('Enter strike'),
#     ],
#     style={
#         'color': colors['text'],
#     }
# )


# Time To Maturity Label
ttm_row11 = html.Td(children=[html.Label('Time to Maturity')],
                    style={
                        'font-size': 20,
                        'textAlign': 'left',
                        'width': '80%',
                        'border': 'None',
                    })

# Time To Maturity dummy
ttm_row12 = html.Td(children=[html.Div('')],
                    style={
                        'width': '20%',
                        'border': 'None',
                    }
                    )

# Time To Maturity slider
ttm_row21 = html.Td(children=[dcc.Slider(id='time-to-maturity-input',
                                         min=1,
                                         max=5,
                                         value=3,
                                         marks={'1': '1m', '2': '3m', '3': '6m', '4': '1y', '5': '2y'}
                                         ),
                              ],
                    style={
                        'width': '100%',
                        'textAlign': 'center',
                        'border': 'None',
                    }
                    )

# Time To Maturity output
ttm_row22 = html.Td(children=[html.Div(id='time-to-maturity-output')],
                    style={
                        'width': '20%',
                        'background-color': output_colors['background'],
                        'font-size': 20,
                        'textAlign': 'center',
                        'border': 'None',
                        'margin-right': '50px'
                    })

time_to_maturity_component = html.Div(children=[
    html.Table(children=[
        html.Tr(children=[ttm_row11, ttm_row12], style={'width': '100%'}),
        html.Tr(children=[ttm_row21, ttm_row22], style={'width': '100%'})
    ],
        # table style
        style={'margin': '20px'}
    )
])

# Implemented as Div -> Table -> 2 rows [Row1 - Label, Row2 - Slider+ChosenValue]
# time_to_maturity_component = html.Div(
#     children=[
#
#         # Table of 2 rows - Label, Slider+ChosenValue
#         html.Table(children=[
#
#             # first row - Label
#             html.Tr(children=[
#                 html.Label('Time to Maturity', style={'font-size': 20}),
#             ]),
#
#             # second row - slider + ChosenValue
#             html.Tr(children=[
#
#                 # slider
#                 html.Td(children=[
#                     dcc.Slider(id='time-to-maturity-input',
#                                min=1,
#                                max=5,
#                                value=3,
#                                marks={'1': '1m', '2': '3m', '3': '6m', '4': '1y', '5': '2y'}
#                                ),
#                 ],
#                     style={
#                         'width': '100%',
#                         'border': 'None',
#                     }),
#
#                 # ChosenValue
#                 html.Td(children=[
#                     html.Div(id='time-to-maturity-output', style={'textAlign': 'Right'}),
#                 ],
#                     # second-row style
#                     style={
#                         'border': 'None',
#                         'width': '100%'
#                     }),
#             ]),  # second-row end
#
#         ],
#             # table-style
#             style={
#                 'border': 'None',
#                 'color': colors['text'],
#             }
#         ),  # table-end
#     ],  # div-children end
#
#     # div-style
#     style={
#         'color': colors['text'],
#     }
# )

# Risk Free Rate
# risk_free_rate_component = html.Div(
#     children=[
#         html.Label('RiskFree Rate (in %)', style={'textAlign': 'Center', 'font-size': 20}),
#         dcc.Slider(id='risk-free-rate-input',
#                    min=0,
#                    max=5,
#                    value=1,
#                    step=0.1,
#                    marks={0: '0%', 1: '1%', 2: '2%', 3: '3%', 4: '4%', 5: '5%'}
#                    ),
#         html.Div(id='risk-free-rate-output', style={'textAlign': 'Center'}),
#         # dcc.Input(id='risk-free-rate-input', type='text', value=1, style={'width': '90%'}),
#         # html.Label('Enter strike'),
#     ],
#     style={'border': '1px',
#            'color': colors['text'],
#            }
# )

# Risk Free Rate Label
rfr_row11 = html.Td(children=[html.Label('RiskFree Rate (in %)')],
                    style={
                        'font-size': 20,
                        'textAlign': 'left',
                        'width': '80%',
                        'border': 'None',
                    })

# Risk Free Rate dummy
rfr_row12 = html.Td(children=[html.Div('')],
                    style={
                        'width': '20%',
                        'border': 'None',
                    }
                    )

# Risk Free Rate slider
rfr_row21 = html.Td(children=[dcc.Slider(id='risk-free-rate-input',
                                         min=1,
                                         max=3,
                                         value=1,
                                         step=0.1,
                                         marks={1: '1%', 2: '2%', 3: '3%'}
                                         ),
                              ],
                    style={
                        'width': '100%',
                        'textAlign': 'center',
                        'border': 'None',
                    }
                    )

# Risk Free Rate output
rfr_row22 = html.Td(children=[html.Div(id='risk-free-rate-output')],
                    style={
                        'width': '20%',
                        'background-color': output_colors['background'],
                        'font-size': 20,
                        'textAlign': 'center',
                        'border': 'None',
                        'margin-right': '50px'
                    })

risk_free_rate_component = html.Div(children=[
    html.Table(children=[
        html.Tr(children=[rfr_row11, rfr_row12], style={'width': '100%'}),
        html.Tr(children=[rfr_row21, rfr_row22], style={'width': '100%'})
    ],
        # table style
        style={'margin': '20px'}
    )
])

# Implemented as Div -> Table -> 2 rows [Row1 - Label, Row2 - Slider+ChosenValue]
# risk_free_rate_component = html.Div(
#     children=[
#
#         # Table of 2 rows - Label, Slider+ChosenValue
#         html.Table(children=[
#
#             # first row - Label
#             html.Tr(children=[
#                 html.Label('RiskFree Rate (in %)', style={'font-size': 20}),
#             ]),
#
#             # second row - slider + ChosenValue
#             html.Tr(children=[
#
#                 # slider
#                 html.Td(children=[
#                     dcc.Slider(id='risk-free-rate-input',
#                                min=0,
#                                max=5,
#                                value=1,
#                                step=0.1,
#                                marks={0: '0%', 1: '1%', 2: '2%', 3: '3%', 4: '4%', 5: '5%'}
#                                ),
#                 ],
#                     style={
#                         'width': '100%',
#                         'border': 'None',
#                     }),
#
#                 # ChosenValue
#                 html.Td(children=[
#                     html.Div(id='risk-free-rate-output', style={'textAlign': 'Right'}),
#                 ],
#                     # second-row style
#                     style={
#                         'border': 'None',
#                         'width': '100%'
#                     }),
#             ]),  # second-row end
#
#         ],
#             # table-style
#             style={
#                 'border': 'None',
#                 'color': colors['text'],
#             }
#         ),  # table-end
#     ],  # div-children end
#
#     # div-style
#     style={
#         'color': colors['text'],
#     }
# )

# Dividend Yield
# dividend_yield_component = html.Div(
#     children=[
#         html.Label('Dividend Yield (in %)', style={'textAlign': 'Center', 'font-size': 20}),
#         dcc.Slider(id='dividend-yield-input',
#                    min=0,
#                    max=5,
#                    value=0,
#                    step=0.1,
#                    marks={0: '0%', 1: '1%', 2: '2%', 3: '3%', 4: '4%', 5: '5%'}
#                    ),
#         html.Div(id='dividend-yield-output', style={'textAlign': 'Center'}),
#         # html.Label('Enter strike'),
#     ],
#     style={'border': '1px',
#            'color': colors['text'],
#            }
# )

# Dividend Yield Label
dy_row11 = html.Td(children=[html.Label('Dividend Yield (in %)')],
                   style={
                       'font-size': 20,
                       'textAlign': 'left',
                       'width': '80%',
                       'border': 'None',
                   })

# Risk Free Rate dummy
dy_row12 = html.Td(children=[html.Div('')],
                   style={
                       'width': '20%',
                       'border': 'None',
                   }
                   )

# Risk Free Rate slider
dy_row21 = html.Td(children=[dcc.Slider(id='dividend-yield-input',
                                        min=0,
                                        max=3,
                                        value=0,
                                        step=0.1,
                                        marks={0: '0%', 1: '1%', 2: '2%', 3: '3%'}
                                        ),
                             ],
                   style={
                       'width': '100%',
                       'textAlign': 'center',
                       'border': 'None',
                   }
                   )

# Risk Free Rate output
dy_row22 = html.Td(children=[html.Div(id='dividend-yield-output')],
                   style={
                       'width': '20%',
                       'background-color': output_colors['background'],
                       'font-size': 20,
                       'textAlign': 'center',
                       'border': 'None',
                       'margin-right': '50px'
                   })

dividend_yield_component = html.Div(children=[
    html.Table(children=[
        html.Tr(children=[dy_row11, dy_row12], style={'width': '100%'}),
        html.Tr(children=[dy_row21, dy_row22], style={'width': '100%'})
    ],
        # table style
        style={'margin': '20px'}
    )
])

# Implied Label
vol_row11 = html.Td(children=[html.Label('Volatility (in %)')],
                    style={
                        'font-size': 20,
                        'textAlign': 'left',
                        'width': '80%',
                        'border': 'None',
                    })

# Risk Free Rate dummy
vol_row12 = html.Td(children=[html.Div('')],
                    style={
                        'width': '20%',
                        'border': 'None',
                    }
                    )

# Risk Free Rate slider
# vol_row21 = html.Td(children=[dcc.Slider(id='dividend-yield-input',
#                                          min=0,
#                                          max=3,
#                                          value=0,
#                                          step=0.1,
#                                          marks={0: '0%', 1: '1%', 2: '2%', 3: '3%'}
#                                          ),
#                               ],
#                     style={
#                         'width': '100%',
#                         'textAlign': 'center',
#                         'border': 'None',
#                     }
#                     )

vol_row21 = html.Td(children=[dcc.Slider(id='vol-input',
                                         min=20,
                                         max=60,
                                         value=30,
                                         marks={20: '20',
                                                30: '30',
                                                40: '40',
                                                50: '50',
                                                60: '60',
                                                }),
                              ],
                    style={
                        'width': '100%',
                        'textAlign': 'center',
                        'border': 'None',
                    }
                    )

# Risk Free Rate output
vol_row22 = html.Td(children=[html.Div(id='vol-output')],
                    style={
                        'width': '20%',
                        'background-color': output_colors['background'],
                        'font-size': 20,
                        'textAlign': 'center',
                        'border': 'None',
                        'margin-right': '50px'
                    })

vol_component = html.Div(children=[
    html.Table(children=[
        html.Tr(children=[vol_row11, vol_row12], style={'width': '100%'}),
        html.Tr(children=[vol_row21, vol_row22], style={'width': '100%'})
    ],
        # table style
        style={'margin': '20px'}
    )
])

# dividend_yield_component = html.Div(
#     children=[
#
#         # Table of 2 rows - Label, Slider+ChosenValue
#         html.Table(children=[
#
#             # first row - Label
#             html.Tr(children=[
#                 html.Label('Dividend Yield (in %)', style={'font-size': 20}),
#             ]),
#
#             # second row - slider + ChosenValue
#             html.Tr(children=[
#
#                 # slider
#                 html.Td(children=[
#                     dcc.Slider(id='dividend-yield-input',
#                                min=0,
#                                max=5,
#                                value=0,
#                                step=0.1,
#                                marks={0: '0%', 1: '1%', 2: '2%', 3: '3%', 4: '4%', 5: '5%'}
#                                ),
#                 ],
#                     style={
#                         'width': '100%',
#                         'border': 'None',
#                     }),
#
#                 # ChosenValue
#                 html.Td(children=[
#                     html.Div(id='dividend-yield-output', style={'textAlign': 'Right'}),
#                 ],
#                     # second-row style
#                     style={
#                         'border': 'None',
#                         'width': '100%'
#                     }),
#             ]),  # second-row end
#
#         ],
#             # table-style
#             style={
#                 'border': 'None',
#                 'color': colors['text'],
#             }
#         ),  # table-end
#     ],  # div-children end
#
#     # div-style
#     style={
#         'color': colors['text'],
#     }
# )

trade_params_pane = html.Div(
    children=[
        html.H5('Trade and Market Parameters', style={'textAlign': 'left', 'margin-left': '10px'}),
        strike_component,
        # html.Br(),
        spot_component,
        # html.Br(),
        time_to_maturity_component,
        # html.Br(),
        risk_free_rate_component,
        # html.Br(),
        # dividend_yield_component,
        vol_component,
        # html.Br(),
    ],
    style={
        'color': pane_colors['text'],
        'background-color': pane_colors['background'],
        'font-family': pane_colors['font-family'],
        'border-color': '#FF0000',
        'margin': '2px',
    }
)


def get_monte_carlo_pricer_pane(app):
    return html.Div(
        children=[
            html.H5('Pricing using Monte Carlo', style={'textAlign': 'left', 'margin-left': '10px'}),

            html.Br(),

            # We wrap Img in Div to center align it
            html.Div(html.Img(src=app.get_asset_url('monte-carlo4.png'), style={'width': '80%'}),
                     style={'textAlign': 'center'}),

            # html.Br(),

            # We wrap Tr in Div so that can control border and margin
            html.Div(children=[

                # We put in Tr so as to get tiles horizontally stacked
                html.Tr(children=[

                    # We wrap Markdown in Td so that to control width - Only 'Tr+Td' combination can give desired width
                    html.Td(dcc.Markdown(id='monte-carlo-price-input'),
                            style={'width': '60%',
                                   'border': 'None'}
                            ),

                    # We wrap Loading in Td so that to control width - Only 'Tr+Td' combination can give desired width
                    html.Td(
                        dcc.Loading(
                            children=[dcc.Markdown(id='monte-carlo-price-output',
                                                   style={
                                                       'textAlign': 'left',
                                                   })],
                            type='circle'
                        ),
                        style={
                            'width': '40%',
                            'border': 'None',
                        }
                    )
                ],
                    # Tr (row) style - width sum to the parts above
                    style={
                        'width': '100%',
                        'border': 'None',
                    }
                )
            ],
                # div style
                style={
                    'textAlign': 'center',
                    'margin': '20px',
                    'border': 'None',
                }
            ),

            # We wrap the Button in Div to center-align it
            html.Div(children=[
                html.Button('Get Price', id='monte-carlo-submit-val', n_clicks=0)
            ],
                style={'textAlign': 'center'}
            ),

            html.Br(),

        ],
        style={
            'color': colors['text'],
            'height': '100%',
            'background-color': pane_colors['background'],
            'font-family': pane_colors['font-family'],
            'border-color': '#FF0000',
            'margin-left': '20px',
        }
    )


def get_deep_learning_pricer_pane(app):
    return html.Div(
        children=[
            html.H5('Pricing using Deep Learning', style={'textAlign': 'left', 'margin-left': '10px'}),

            html.Br(),

            # We wrap Img in Div to center align it
            html.Div(html.Img(src=app.get_asset_url('deep-learning4.png'), style={'width': '80%'}),
                     style={'textAlign': 'center'}),

            # We wrap Tr in Div so that can control border and margin
            html.Div(children=[

                # We put in Tr so as to get tiles horizontally stacked
                html.Tr(children=[

                    # We wrap Markdown in Td so that to control width - Only 'Tr+Td' combination can give desired width
                    html.Td(dcc.Markdown(id='deep-learning-price-input'),
                            style={'width': '60%',
                                   'border': 'None'}
                            ),

                    # We wrap Loading in Td so that to control width - Only 'Tr+Td' combination can give desired width
                    html.Td(children=[dcc.Markdown(id='deep-learning-price-output',
                                                   style={
                                                       'textAlign': 'left',
                                                   })],
                            style={
                                'width': '40%',
                                'border': 'None',
                            }
                            )
                ],
                    # Tr (row) style - width sum to the parts above
                    style={
                        'width': '100%',
                        'border': 'None',
                    }
                )
            ],
                # div style
                style={
                    'textAlign': 'center',
                    'margin': '20px',
                    'border': 'None',
                }
            ),

            html.Br(),
            html.Br(),

        ],
        style={
            'color': colors['text'],
            'background-color': pane_colors['background'],
            'font-family': pane_colors['font-family'],
            'border-color': '#FF0000',
        }
    )


# header_top_component = html.Div('', style={'background-color': colors['background']})
# header_top_component = html.Div('SNAP dashboard', style={'color': colors['text']})
header_top_component = html.Br()

header_component = html.Div(
    children=[
        # Header
        # html.Div('', style={'background-color': colors['background']}),
        html.Br(),
        html.H2(
            children='SNAP (demo)',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'margin-left': '20px',
                'font-family': 'serif',
            }
        ),
        # html.Br(),

        # Sub-header
        dcc.Markdown('''
        Pricing Vanilla Call options  
        **Monte Carlo vs Deep Learning**
        ''',
                     style={
                         'textAlign': 'left',
                         'color': colors['text'],
                         'font-size': 18,
                         'margin-left': '20px',
                     }
                     ),

        html.Br(),
        # html.P(
        #     children=['Pricing S&P call options'],
        #     style={
        #         'textAlign': 'left',
        #         'color': colors['text'],
        #         'font-size': 18,
        #         'margin-left': '20px',
        #     }
        # ),
        #
        # # Sub-header
        # html.P(
        #     children=['Slow Monte Carlo vs Real Time Deep Learning Pricers'],
        #     style={
        #         'textAlign': 'left',
        #         'color': colors['text'],
        #         'font-size': 18,
        #         'margin-left': '20px',
        #     }
        # ),

    ], style={
        'background-image': header_colors['background-image'],
        # 'background-color': header_colors['background'],
    }
)

snap_description_component = html.P('''
    Traditional Monte Carlo based valuations are very costly to compute.
    SNAP uses deep learning to learn a numerical representation of the target model.
    The result is fast and accurate valuations and risk sensitivities.
''',
                                    style={
                                        'width': '60%',
                                        'font-size': 20,
                                        'font-family': 'calibri',
                                        'color': colors['text'],
                                        'margin-left': '20px',
                                    },
                                    )
