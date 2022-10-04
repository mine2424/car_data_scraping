
// import excel "/Users/mine/development/goo_car_scraping/data/f_medi_all_light_rv_car_data_by_all_grade.xlsx", sheet("eKdays_lower_median") firstrow

//import excel "/Users/mine/development/goo_car_scraping/data/f_medi_all_light_rv_car_data_by_all_grade.xlsx", sheet("eKdays_higher_median") firstrow

rename 年 year
rename 月 month
rename メーカー maker
rename 台数 quantity
rename 通称名 car_name
rename グレード grade
rename マイナーチェンジ minor_change
rename 型番 model_number
rename 車種 car_model
rename 新車価格 new_car_price
rename 実質価格CPI2007基準 real_price
rename 排気量 exhaust
rename トランスミッション mission
rename 乗車定員 people
rename ハイブリット hybrid
rename 最高出力kW kw
rename メーカー標準ボディカラー maker_normal_body_color
rename メーカーオプションボディカラー maker_option_body_color
rename 過給機 d_turbo
rename 燃費WLTC fuel_wltc
rename 燃費JC08 fuel_jc08
rename 燃費1015 fuel_1015
rename 全長 lengtht
rename 全幅 width
rename 全高 height
rename サイズ size
rename 車両重量 weight

// mission dummy
// FF -> 0, FULL4WD -> 1
generate d_4wd = 1 if mission == "FULL4WD"
replace d_4wd = 0 if mission == "FF"

// long型に変換する??


