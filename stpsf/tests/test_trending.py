import astropy
import astropy.time
import astropy.units as u
import stpsf


def test_monthly_trending_plot_auto_opdtable():
    trend_table = stpsf.trending.monthly_trending_plot(2023, 6, instrument='NIRISS', filter='F380M')
    assert len(trend_table) == 15


def test_monthly_trending_plot_opdtable_param():
    # Get broad range opdtable to verify our internal filtering works
    start_date, end_date = stpsf.trending.get_month_start_end(2023, 5)
    start_date2, end_date2 = stpsf.trending.get_month_start_end(2023, 7)
    # Start a little early, such that we are going to have at least 1 WFS before the start date
    pre_start_date = astropy.time.Time(start_date) - astropy.time.TimeDelta(4 * u.day)

    # Retrieve full OPD table, then trim to the selected time period
    opdtable0 = stpsf.mast_wss.retrieve_mast_opd_table()
    opdtable0 = stpsf.mast_wss.deduplicate_opd_table(opdtable0)
    opdtable = stpsf.mast_wss.filter_opd_table(opdtable0, start_time=pre_start_date, end_time=end_date2)
    trend_table = stpsf.trending.monthly_trending_plot(2023, 6, opdtable=opdtable, instrument='NIRISS', filter='F380M')
    assert len(trend_table) == 15


def test_delta_wfe_around_time():
    """Very basic test - does this hand back something that could be an OPD array
    Does not check the value in any significant way.
    """
    opd = stpsf.trending.delta_wfe_around_time('2024-02-26')
    assert opd.shape == (256, 256), 'this function should return an OPD with the expected size'
