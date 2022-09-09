class CarSpecTable:
    def __init__(self) -> None:
        # メーカー
        self.manufacturer

        # 車種
        self.car_model

        # 車名
        self.car_name

        # グレード
        self.grade

        # 新車価格
        # (以下からが取得するデータの内容)
        self.new_car_price

        # 発売日
        self.release_date

        # 発売区分
        self.release_classification

        # 新車販売状況
        self.new_car_sales_status

        # 駆動方式
        self.drivetrain

        # 型式
        self.model

        # 燃料
        self.fuel

        # 動力分類
        self.power_classification

        # 燃料タンク容量
        self.fuel_tank_capacity

        # 排気量
        self.displacement

        # トランスミッション
        self.transmission

        # 乗車定員
        self.seating_capacity

        # ドア数
        self.number_of_doors

        # シート列数
        self.number_of_rows_of_seats

        # 燃費（WLTCモード）
        self.fuel_economy_in_WLTC_mode

        # 燃費（WLTCモード|市街地）
        self.fuel_economy_in_WLTC_mode_urban

        # 燃費（WLTCモード|郊外）
        self.fuel_economy_in_WLTC_mode_suburban

        # 燃費（WLTCモード|高速道路）
        self.fuel_economy_WLTC_mode_highway

        # WLTC Co2排出量
        self.WLTC_Co2_emissions

        # 燃費（JC08モード）
        self.fuel_economy_in_JC08_mode

        # 燃費（10.15モード）
        self.fuel_economy_1015_mode

        # 充電走行距離（km）
        self.Charge_mileage_by_km

        # ハンドル位置
        self.steering_wheel_position

        # 最小回転半径
        self.minimum_turning_radius

        # 最高出力(kW[PS]/rpm)
        self.maximum_output_by_kW_PS_by_rpm

        # 最高トルク(N・m[kgf・m]/rpm)
        self.maximum_torque_by_N_m_kgf_m_by_rpm

        # 過給機
        self.supercharger

        # アイドリングストップ
        self.idling_stop

        # 総電力量(kWh)
        self.total_electric_power_by_kWh

        # 最高出力(kW[PS])
        self.maximum_power_output_by_kW_PS

        # 最高トルク(N・m[kgf・m])
        self.maximum_torque_by_N_m_kgf_m

        # 200V充電時間
        self.two_hundred_volt_charging_time

        # 急速充電時間
        self.fast_charge_time

        # 自動車税
        self.vehicle_tax

        # 自動車重量税
        self.vehicle_weight_tax

        # 自動車取得税
        self.vehicle_acquisition_tax

        # 環境性能割
        self.environmental_performance_rate

        # 全長
        self.overall_length

        # 全幅
        self.overall_width

        # 全高
        self.overall_height

        # ホイールベース
        self.wheelbase

        # 最低地上高（未積載時）
        self.minimum_ground_clearance_by_unloaded

        # 車両重量
        self.vehicle_weight

        # 車両総重量
        self.gross_vehicle_weight

        # 室内長
        self. interior_length

        # 室内高
        self.interior_height

        # ヘッドルーム 前
        self.headroom_front

        # ヘッドルーム 後
        self.headroom_rear

        # 荷室容量（リアシート立）
        self.cargo_capacity_by_rear_seat_upright

        # 荷室容量（リアシート倒）
        self.cargo_capacity_by_rear_seat_down

        # 荷室容量 測定方式
        self.tire_size_front

        # リアシートまでの長さ
        self.tire_size_rear

        # ホイールサイズ 前
        self.tread_width_front

        # ホイールサイズ 後
        self.tire_size_before

        # タイヤサイズ 前
        self.tread_width_after

        # タイヤサイズ 後
        self.tire_size_after

        # トレッド幅 前
        self.tread_width_before

        # トレッド幅 後
        self.tread_width_after

        # アルミホイール
        self.aluminum_wheel

        # スペアタイヤ
        self.spare_tire

        # パンク修理キット
        self.flat_tire_repair_kit

        # 空気圧警告灯
        self.air_pressure_warning_light

        # 燃費基準達成率
        self.fuel_economy_standard_achievement_rate

        # 自動車税減税率
        self.automobile_tax_reduction_rate

        # 自動車重量税減税率
        self.vehicle_weight_tax_reduction_rate

        # 取得税減税率
        self.acquisition_tax_reduction_rate

        # 環境性能割税率
        self.environmental_performance_discount_rate

    def copy_with(self, manufacturer, car_model, car_name, grade, new_car_price, release_date, release_classification, new_car_sales_status, drivetrain, model, fuel, power_classification, fuel_tank_capacity, displacement, transmission, seating_capacity, number_of_doors, number_of_rows_of_seats, fuel_economy_in_WLTC_mode, fuel_economy_in_WLTC_mode_urban, fuel_economy_in_WLTC_mode_suburban, fuel_economy_WLTC_mode_highway, WLTC_Co2_emissions, fuel_economy_in_JC08_mode, fuel_economy_1015_mode, Charge_mileage_by_km, steering_wheel_position, minimum_turning_radius, maximum_output_by_kW_PS_by_rpm, maximum_torque_by_N_m_kgf_m_by_rpm, supercharger, idling_stop, total_electric_power_by_kWh, maximum_power_output_by_kW_PS, maximum_torque_by_N_m_kgf_m, two_hundred_volt_charging_time, fast_charge_time, vehicle_tax, vehicle_weight_tax, vehicle_acquisition_tax, environmental_performance_rate, overall_length, overall_width, overall_height, wheelbase, minimum_ground_clearance_by_unloaded, vehicle_weight, gross_vehicle_weight, interior_length, interior_height, headroom_front, headroom_rear, cargo_capacity_by_rear_seat_upright, cargo_capacity_by_rear_seat_down, tire_size_front, tire_size_rear, tread_width_front, tire_size_before, tread_width_after, tire_size_after, tread_width_before, aluminum_wheel, spare_tire, flat_tire_repair_kit, air_pressure_warning_light, fuel_economy_standard_achievement_rate, automobile_tax_reduction_rate, vehicle_weight_tax_reduction_rate, acquisition_tax_reduction_rate, environmental_performance_discount_rate):

        if not manufacturer and not self.manufacturer:
            self.manufacturer = ''
        else:
            self.manufacturer = manufacturer

        if not car_model and not self.car_model:
            self.car_model = ''
        else:
            self.car_model = car_model

        if not car_name and not self.car_name:
            self.car_name = ''
        else:
            self.car_name = car_name

        if not grade and not self.grade:
            self.grade = ''
        else:
            self.grade = grade

        if not new_car_price and not self.new_car_price:
            self.new_car_price = ''
        else:
            self.new_car_price = new_car_price

        if not release_date and not self.release_date:
            self.release_date = ''
        else:
            self.release_date = release_date

        if not release_classification and not self.release_classification:
            self.release_classification = ''
        else:
            self.release_classification = release_classification

        if not new_car_sales_status and not self.new_car_sales_status:
            self.new_car_sales_status = ''
        else:
            self.new_car_sales_status = new_car_sales_status

        if not drivetrain and not self.drivetrain:
            self.drivetrain = ''
        else:
            self.drivetrain = drivetrain

        if not model and not self.model:
            self.model = ''
        else:
            self.model = model

        if not fuel and not self.fuel:
            self.fuel = ''
        else:
            self.fuel = fuel

        if not power_classification and not self.power_classification:
            self.power_classification = ''
        else:
            self.power_classification = power_classification

        if not fuel_tank_capacity and not self.fuel_tank_capacity:
            self.fuel_tank_capacity = ''
        else:
            self.fuel_tank_capacity = fuel_tank_capacity

        if not displacement and not self.displacement:
            self.displacement = ''
        else:
            self.displacement = displacement

        if not transmission and not self.transmission:
            self.transmission = ''
        else:
            self.transmission = transmission

        if not seating_capacity and not self.seating_capacity:
            self.seating_capacity = ''
        else:
            self.seating_capacity = seating_capacity

        if not number_of_doors and not self.number_of_doors:
            self.number_of_doors = ''
        else:
            self.number_of_doors = number_of_doors

        if not number_of_rows_of_seats and not self.number_of_rows_of_seats:
            self.number_of_rows_of_seats = ''
        else:
            self.number_of_rows_of_seats = number_of_rows_of_seats

        if not fuel_economy_in_WLTC_mode and not self.fuel_economy_in_WLTC_mode:
            self.fuel_economy_in_WLTC_mode = ''
        else:
            self.fuel_economy_in_WLTC_mode = fuel_economy_in_WLTC_mode

        if not fuel_economy_in_WLTC_mode_urban and not self.fuel_economy_in_WLTC_mode_urban:
            self.fuel_economy_in_WLTC_mode_urban = ''
        else:
            self.fuel_economy_in_WLTC_mode_urban = fuel_economy_in_WLTC_mode_urban

        if not fuel_economy_in_WLTC_mode_suburban and not self.fuel_economy_in_WLTC_mode_suburban:
            self.fuel_economy_in_WLTC_mode_suburban = ''
        else:
            self.fuel_economy_in_WLTC_mode_suburban = fuel_economy_in_WLTC_mode_suburban

        if not fuel_economy_WLTC_mode_highway and not self.fuel_economy_WLTC_mode_highway:
            self.fuel_economy_WLTC_mode_highway = ''
        else:
            self.fuel_economy_WLTC_mode_highway = fuel_economy_WLTC_mode_highway

        if not WLTC_Co2_emissions and not self.WLTC_Co2_emissions:
            self.WLTC_Co2_emissions = ''
        else:
            self.WLTC_Co2_emissions = WLTC_Co2_emissions

        if not fuel_economy_in_JC08_mode and not self.fuel_economy_in_JC08_mode:
            self.fuel_economy_in_JC08_mode = ''
        else:
            self.fuel_economy_in_JC08_mode = fuel_economy_in_JC08_mode

        if not fuel_economy_1015_mode and not self.fuel_economy_1015_mode:
            self.fuel_economy_1015_mode = ''
        else:
            self.fuel_economy_1015_mode = fuel_economy_1015_mode

        if not Charge_mileage_by_km and not self.Charge_mileage_by_km:
            self.Charge_mileage_by_km = ''
        else:
            self.Charge_mileage_by_km = Charge_mileage_by_km

        if not steering_wheel_position and not self.steering_wheel_position:
            self.steering_wheel_position = ''
        else:
            self.steering_wheel_position = steering_wheel_position

        if not minimum_turning_radius and not self.minimum_turning_radius:
            self.minimum_turning_radius = ''
        else:
            self.minimum_turning_radius = minimum_turning_radius

        if not maximum_output_by_kW_PS_by_rpm and not self.maximum_output_by_kW_PS_by_rpm:
            self.maximum_output_by_kW_PS_by_rpm = ''
        else:
            self.maximum_output_by_kW_PS_by_rpm = maximum_output_by_kW_PS_by_rpm

        if not maximum_torque_by_N_m_kgf_m_by_rpm and not self.maximum_torque_by_N_m_kgf_m_by_rpm:
            self.maximum_torque_by_N_m_kgf_m_by_rpm = ''
        else:
            self.maximum_torque_by_N_m_kgf_m_by_rpm = maximum_torque_by_N_m_kgf_m_by_rpm

        if not supercharger and not self.supercharger:
            self.supercharger = ''
        else:
            self.supercharger = supercharger

        if not idling_stop and not self.idling_stop:
            self.idling_stop = ''
        else:
            self.idling_stop = idling_stop

        if not total_electric_power_by_kWh and not self.total_electric_power_by_kWh:
            self.total_electric_power_by_kWh = ''
        else:
            self.total_electric_power_by_kWh = total_electric_power_by_kWh

        if not maximum_power_output_by_kW_PS and not self.maximum_power_output_by_kW_PS:
            self.maximum_power_output_by_kW_PS = ''
        else:
            self.maximum_power_output_by_kW_PS = maximum_power_output_by_kW_PS

        if not maximum_torque_by_N_m_kgf_m and not self.maximum_torque_by_N_m_kgf_m:
            self.maximum_torque_by_N_m_kgf_m = ''
        else:
            self.maximum_torque_by_N_m_kgf_m = maximum_torque_by_N_m_kgf_m

        if not two_hundred_volt_charging_time and not self.two_hundred_volt_charging_time:
            self.two_hundred_volt_charging_time = ''
        else:
            self.two_hundred_volt_charging_time = two_hundred_volt_charging_time

        if not fast_charge_time and not self.fast_charge_time:
            self.fast_charge_time = ''
        else:
            self.fast_charge_time = fast_charge_time

        if not vehicle_tax and not self.vehicle_tax:
            self.vehicle_tax = ''
        else:
            self.vehicle_tax = vehicle_tax

        if not vehicle_weight_tax and not self.vehicle_weight_tax:
            self.vehicle_weight_tax = ''
        else:
            self.vehicle_weight_tax = vehicle_weight_tax

        if not vehicle_acquisition_tax and not self.vehicle_acquisition_tax:
            self.vehicle_acquisition_tax = ''
        else:
            self.vehicle_acquisition_tax = vehicle_acquisition_tax

        if not environmental_performance_rate and not self.environmental_performance_rate:
            self.environmental_performance_rate = ''
        else:
            self.environmental_performance_rate = environmental_performance_rate

        if not overall_length and not self.overall_length:
            self.overall_length = ''
        else:
            self.overall_length = overall_length

        if not overall_width and not self.overall_width:
            self.overall_width = ''
        else:
            self.overall_width = overall_width

        if not overall_height and not self.overall_height:
            self.overall_height = ''
        else:
            self.overall_height = overall_height

        if not wheelbase and not self.wheelbase:
            self.wheelbase = ''
        else:
            self.wheelbase = wheelbase

        if not minimum_ground_clearance_by_unloaded and not self.minimum_ground_clearance_by_unloaded:
            self.minimum_ground_clearance_by_unloaded = ''
        else:
            self.minimum_ground_clearance_by_unloaded = minimum_ground_clearance_by_unloaded

        if not vehicle_weight and not self.vehicle_weight:
            self.vehicle_weight = ''
        else:
            self.vehicle_weight = vehicle_weight

        if not gross_vehicle_weight and not self.gross_vehicle_weight:
            self.gross_vehicle_weight = ''
        else:
            self.gross_vehicle_weight = gross_vehicle_weight

        if not interior_length and not self.interior_length:
            self. interior_length = ''
        else:
            self. interior_length = interior_length

        if not interior_height and not self.interior_height:
            self.interior_height = ''
        else:
            self.interior_height = interior_height

        if not headroom_front and not self.headroom_front:
            self.headroom_front = ''
        else:
            self.headroom_front = headroom_front

        if not headroom_rear and not self.headroom_rear:
            self.headroom_rear = ''
        else:
            self.headroom_rear = headroom_rear

        if not cargo_capacity_by_rear_seat_upright and not self.cargo_capacity_by_rear_seat_upright:
            self.cargo_capacity_by_rear_seat_upright = ''
        else:
            self.cargo_capacity_by_rear_seat_upright = cargo_capacity_by_rear_seat_upright

        if not cargo_capacity_by_rear_seat_down and not self.cargo_capacity_by_rear_seat_down:
            self.cargo_capacity_by_rear_seat_down = ''
        else:
            self.cargo_capacity_by_rear_seat_down = cargo_capacity_by_rear_seat_down

        if not tire_size_front and not self.tire_size_front:
            self.tire_size_front = ''
        else:
            self.tire_size_front = tire_size_front

        if not tire_size_rear and not self.tire_size_rear:
            self.tire_size_rear = ''
        else:
            self.tire_size_rear = tire_size_rear

        if not tread_width_front and not self.tread_width_front:
            self.tread_width_front = ''
        else:
            self.tread_width_front = tread_width_front

        if not tire_size_before and not self.tire_size_before:
            self.tire_size_before = ''
        else:
            self.tire_size_before = tire_size_before

        if not tread_width_after and not self.tread_width_after:
            self.tread_width_after = ''
        else:
            self.tread_width_after = tread_width_after

        if not tire_size_after and not self.tire_size_after:
            self.tire_size_after = ''
        else:
            self.tire_size_after = tire_size_after

        if not tread_width_before and not self.tread_width_before:
            self.tread_width_before = ''
        else:
            self.tread_width_before = tread_width_before

        if not tread_width_after and not self.tread_width_after:
            self.tread_width_after = ''
        else:
            self.tread_width_after = tread_width_after

        if not aluminum_wheel and not self.aluminum_wheel:
            self.aluminum_wheel = ''
        else:
            self.aluminum_wheel = aluminum_wheel

        if not spare_tire and not self.spare_tire:
            self.spare_tire = ''
        else:
            self.spare_tire = spare_tire

        if not flat_tire_repair_kit and not self.flat_tire_repair_kit:
            self.flat_tire_repair_kit = ''
        else:
            self.flat_tire_repair_kit = flat_tire_repair_kit

        if not air_pressure_warning_light and not self.air_pressure_warning_light:
            self.air_pressure_warning_light = ''
        else:
            self.air_pressure_warning_light = air_pressure_warning_light

        if not fuel_economy_standard_achievement_rate and not self.fuel_economy_standard_achievement_rate:
            self.fuel_economy_standard_achievement_rate = ''
        else:
            self.fuel_economy_standard_achievement_rate = fuel_economy_standard_achievement_rate

        if not automobile_tax_reduction_rate and not self.automobile_tax_reduction_rate:
            self.automobile_tax_reduction_rate = ''
        else:
            self.automobile_tax_reduction_rate = automobile_tax_reduction_rate

        if not vehicle_weight_tax_reduction_rate and not self.vehicle_weight_tax_reduction_rate:
            self.vehicle_weight_tax_reduction_rate = ''
        else:
            self.vehicle_weight_tax_reduction_rate = vehicle_weight_tax_reduction_rate

        if not acquisition_tax_reduction_rate and not self.acquisition_tax_reduction_rate:
            self.acquisition_tax_reduction_rate = ''
        else:
            self.acquisition_tax_reduction_rate = acquisition_tax_reduction_rate

        if not environmental_performance_discount_rate and not self.environmental_performance_discount_rate:
            self.environmental_performance_discount_rate = ''
        else:
            self.environmental_performance_discount_rate = environmental_performance_discount_rate
