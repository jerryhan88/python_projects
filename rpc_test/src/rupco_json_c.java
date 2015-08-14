import java.net.URL;
import java.util.ArrayList;

import com.googlecode.jsonrpc4j.JsonRpcHttpClient;

public class rupco_json_c {
	//
	// helpers for input
	//
	public static Object node(String nid, int capa) {
		return new Object[] { nid, new Integer(capa) };
	}

	public static Object lane(String node_from, String node_to,
			double distance, double avg_speed) {
		return new Object[] { node_from, node_to, new Double(distance),
				new Double(avg_speed) };
	}

	public static Object vehicle(String vid, double length, double max_speed,
			String node_from, String node_to, double offset_on_lane) {

		return new Object[] { vid, new Double(length), new Double(max_speed),
				node_from, node_to, new Double(offset_on_lane) };
	}

	public static Object vehicle_info(String vid, String node_from,
			String node_to, double offset_on_lane, String[] path, int vos_state) {
		return new Object[] { vid, node_from, node_to,
				new Double(offset_on_lane), path, new Integer(vos_state) };
	}

	public static Object waiting_info(String nid, String[] customer_indices) {
		return new Object[] { nid, customer_indices };
	}

	public static void main(String[] args) throws Throwable {

		Object[][] nspec = new Object[][] {
				(Object[]) rupco_json_c.node("1132", 1),
				(Object[]) rupco_json_c.node("2313", 3),
				(Object[]) rupco_json_c.node("1339", 3),
				(Object[]) rupco_json_c.node("1413", 1),
				(Object[]) rupco_json_c.node("1501", 1),
				(Object[]) rupco_json_c.node("1512", 1),
				(Object[]) rupco_json_c.node("1599", 3),
				(Object[]) rupco_json_c.node("1667", 1),
				(Object[]) rupco_json_c.node("1739", 3),
				(Object[]) rupco_json_c.node("1885", 1),
				(Object[]) rupco_json_c.node("1975", 3),
				(Object[]) rupco_json_c.node("2023", 3),
				(Object[]) rupco_json_c.node("2070", 1),
				(Object[]) rupco_json_c.node("2111", 3),
				(Object[]) rupco_json_c.node("2173", 3),
				(Object[]) rupco_json_c.node("2231", 1),
				(Object[]) rupco_json_c.node("2286", 3),
				(Object[]) rupco_json_c.node("30", 1),
				(Object[]) rupco_json_c.node("53", 1),
				(Object[]) rupco_json_c.node("84", 1),
				(Object[]) rupco_json_c.node("133", 1),
				(Object[]) rupco_json_c.node("139", 1),
				(Object[]) rupco_json_c.node("249", 1),
				(Object[]) rupco_json_c.node("277", 1),
				(Object[]) rupco_json_c.node("3234", 1),
				(Object[]) rupco_json_c.node("3236", 1),
				(Object[]) rupco_json_c.node("3247", 1),
				(Object[]) rupco_json_c.node("3259", 1),
				(Object[]) rupco_json_c.node("3260", 1),
				(Object[]) rupco_json_c.node("3271", 1),
				(Object[]) rupco_json_c.node("3272", 1),
				(Object[]) rupco_json_c.node("3283", 1),
				(Object[]) rupco_json_c.node("3284", 1),
				(Object[]) rupco_json_c.node("3296", 1),
				(Object[]) rupco_json_c.node("3307", 1),
				(Object[]) rupco_json_c.node("3318", 1),
				(Object[]) rupco_json_c.node("3319", 1),
				(Object[]) rupco_json_c.node("3330", 1),
				(Object[]) rupco_json_c.node("3341", 1),
				(Object[]) rupco_json_c.node("3342", 1),
				(Object[]) rupco_json_c.node("3343", 1),
				(Object[]) rupco_json_c.node("3355", 1),
				(Object[]) rupco_json_c.node("3366", 1),
				(Object[]) rupco_json_c.node("3389", 1),
				(Object[]) rupco_json_c.node("3390", 1),
				(Object[]) rupco_json_c.node("3402", 1),
				(Object[]) rupco_json_c.node("3403", 1),
				(Object[]) rupco_json_c.node("3414", 1),
				(Object[]) rupco_json_c.node("3425", 1),
				(Object[]) rupco_json_c.node("3427", 1),
				(Object[]) rupco_json_c.node("3438", 1),
				(Object[]) rupco_json_c.node("3451", 1),
				(Object[]) rupco_json_c.node("3452", 1),
				(Object[]) rupco_json_c.node("3453", 1),
				(Object[]) rupco_json_c.node("3464", 1),
				(Object[]) rupco_json_c.node("3466", 1),
				(Object[]) rupco_json_c.node("3477", 1),
				(Object[]) rupco_json_c.node("3479", 1),
				(Object[]) rupco_json_c.node("3490", 1),
				(Object[]) rupco_json_c.node("3601", 3),
				(Object[]) rupco_json_c.node("118", 1),
				(Object[]) rupco_json_c.node("3354", 1),
				(Object[]) rupco_json_c.node("3368", 1),
				(Object[]) rupco_json_c.node("2486", 1),
				(Object[]) rupco_json_c.node("2571", 3),
				(Object[]) rupco_json_c.node("2636", 3),
				(Object[]) rupco_json_c.node("2773", 3),
				(Object[]) rupco_json_c.node("3006", 3),
				(Object[]) rupco_json_c.node("3177", 3),
				(Object[]) rupco_json_c.node("3179", 3),
				(Object[]) rupco_json_c.node("3181", 1),
				(Object[]) rupco_json_c.node("3198", 1),
				(Object[]) rupco_json_c.node("3210", 1),
				(Object[]) rupco_json_c.node("3211", 1),
				(Object[]) rupco_json_c.node("3223", 1),
				(Object[]) rupco_json_c.node("205", 1),
				(Object[]) rupco_json_c.node("19", 1),
				(Object[]) rupco_json_c.node("78", 1),
				(Object[]) rupco_json_c.node("149", 1),
				(Object[]) rupco_json_c.node("212", 1),
				(Object[]) rupco_json_c.node("317", 1),
				(Object[]) rupco_json_c.node("335", 1) };

		Object[][] lspec = new Object[][] {
				(Object[]) rupco_json_c.lane("1413", "2173", 27.453, 10.0),
				(Object[]) rupco_json_c.lane("3477", "3466", 18.003, 10.0),
				(Object[]) rupco_json_c.lane("3477", "3451", 117.758, 10.0),
				(Object[]) rupco_json_c.lane("3006", "3354", 66.414, 10.0),
				(Object[]) rupco_json_c.lane("3479", "2486", 145.396, 10.0),
				(Object[]) rupco_json_c.lane("3284", "1339", 54.306, 10.0),
				(Object[]) rupco_json_c.lane("3283", "2111", 36.352, 10.0),
				(Object[]) rupco_json_c.lane("118", "133", 29.999, 6.0),
				(Object[]) rupco_json_c.lane("335", "249", 14.71, 1.0),
				(Object[]) rupco_json_c.lane("335", "139", 77.779, 2.0),
				(Object[]) rupco_json_c.lane("3343", "3354", 20.301, 10.0),
				(Object[]) rupco_json_c.lane("3343", "3368", 118.91, 10.0),
				(Object[]) rupco_json_c.lane("3342", "3341", 20.034, 10.0),
				(Object[]) rupco_json_c.lane("3342", "3366", 117.865, 10.0),
				(Object[]) rupco_json_c.lane("3341", "3318", 144.474, 10.0),
				(Object[]) rupco_json_c.lane("3198", "2286", 14.96, 10.0),
				(Object[]) rupco_json_c.lane("3438", "3427", 18.501, 10.0),
				(Object[]) rupco_json_c.lane("3438", "3464", 118.089, 10.0),
				(Object[]) rupco_json_c.lane("1975", "3236", 92.794, 10.0),
				(Object[]) rupco_json_c.lane("1667", "3259", 152.218, 10.0),
				(Object[]) rupco_json_c.lane("3234", "3211", 103.058, 10.0),
				(Object[]) rupco_json_c.lane("3236", "3247", 19.879, 10.0),
				(Object[]) rupco_json_c.lane("3236", "3479", 126.225, 10.0),
				(Object[]) rupco_json_c.lane("249", "277", 97.213, 1.0),
				(Object[]) rupco_json_c.lane("84", "118", 67.973, 5.0),
				(Object[]) rupco_json_c.lane("3390", "1599", 10.605, 10.0),
				(Object[]) rupco_json_c.lane("3307", "3296", 101.39, 10.0),
				(Object[]) rupco_json_c.lane("205", "212", 12.443, 2.0),
				(Object[]) rupco_json_c.lane("2571", "3438", 34.997, 10.0),
				(Object[]) rupco_json_c.lane("3451", "3414", 77.341, 10.0),
				(Object[]) rupco_json_c.lane("3179", "3490", 100.296, 10.0),
				(Object[]) rupco_json_c.lane("3453", "3464", 19.801, 10.0),
				(Object[]) rupco_json_c.lane("3453", "3427", 117.317, 10.0),
				(Object[]) rupco_json_c.lane("3452", "3451", 21.439, 10.0),
				(Object[]) rupco_json_c.lane("3452", "3466", 118.821, 10.0),
				(Object[]) rupco_json_c.lane("3296", "3284", 21.449, 10.0),
				(Object[]) rupco_json_c.lane("3296", "3283", 92.02, 10.0),
				(Object[]) rupco_json_c.lane("3354", "2231", 108.365, 10.0),
				(Object[]) rupco_json_c.lane("3490", "3479", 19.641, 10.0),
				(Object[]) rupco_json_c.lane("3490", "118", 34.928, 8.0),
				(Object[]) rupco_json_c.lane("3490", "3247", 125.956, 10.0),
				(Object[]) rupco_json_c.lane("1512", "1501", 20.995, 10.0),
				(Object[]) rupco_json_c.lane("1512", "3307", 131.541, 10.0),
				(Object[]) rupco_json_c.lane("277", "2486", 34.522, 5.0),
				(Object[]) rupco_json_c.lane("277", "317", 79.174, 1.0),
				(Object[]) rupco_json_c.lane("30", "53", 46.005, 10.0),
				(Object[]) rupco_json_c.lane("1339", "3271", 47.537, 10.0),
				(Object[]) rupco_json_c.lane("3389", "3390", 20.784, 10.0),
				(Object[]) rupco_json_c.lane("3389", "1667", 130.236, 10.0),
				(Object[]) rupco_json_c.lane("3247", "1885", 164.805, 10.0),
				(Object[]) rupco_json_c.lane("2023", "3453", 32.908, 10.0),
				(Object[]) rupco_json_c.lane("3402", "2070", 21.613, 10.0),
				(Object[]) rupco_json_c.lane("3402", "3425", 127.684, 10.0),
				(Object[]) rupco_json_c.lane("3181", "3179", 32.686, 10.0),
				(Object[]) rupco_json_c.lane("3403", "1667", 21.679, 10.0),
				(Object[]) rupco_json_c.lane("3403", "3390", 129.097, 10.0),
				(Object[]) rupco_json_c.lane("3211", "1132", 20.388, 10.0),
				(Object[]) rupco_json_c.lane("3211", "1413", 150.412, 10.0),
				(Object[]) rupco_json_c.lane("3210", "3198", 19.037, 10.0),
				(Object[]) rupco_json_c.lane("3210", "3234", 124.681, 10.0),
				(Object[]) rupco_json_c.lane("212", "19", 51.622, 8.0),
				(Object[]) rupco_json_c.lane("3319", "3330", 19.084, 10.0),
				(Object[]) rupco_json_c.lane("3319", "3260", 130.509, 10.0),
				(Object[]) rupco_json_c.lane("133", "139", 11.957, 4.0),
				(Object[]) rupco_json_c.lane("133", "30", 16.623, 10.0),
				(Object[]) rupco_json_c.lane("139", "149", 18.76, 4.0),
				(Object[]) rupco_json_c.lane("3260", "3452", 143.192, 10.0),
				(Object[]) rupco_json_c.lane("19", "30", 21.865, 15.0),
				(Object[]) rupco_json_c.lane("2070", "3272", 157.732, 10.0),
				(Object[]) rupco_json_c.lane("317", "84", 10.527, 2.0),
				(Object[]) rupco_json_c.lane("317", "335", 44.094, 1.0),
				(Object[]) rupco_json_c.lane("3464", "3223", 165.209, 10.0),
				(Object[]) rupco_json_c.lane("1885", "3368", 21.709, 10.0),
				(Object[]) rupco_json_c.lane("1885", "3006", 53.662, 10.0),
				(Object[]) rupco_json_c.lane("3601", "2773", 187.63, 10.0),
				(Object[]) rupco_json_c.lane("2231", "3181", 116.246, 10.0),
				(Object[]) rupco_json_c.lane("2313", "1501", 71.382, 10.0),
				(Object[]) rupco_json_c.lane("1599", "3342", 67.338, 10.0),
				(Object[]) rupco_json_c.lane("3318", "3307", 20.302, 10.0),
				(Object[]) rupco_json_c.lane("3318", "2313", 58.876, 10.0),
				(Object[]) rupco_json_c.lane("3355", "3366", 19.158, 10.0),
				(Object[]) rupco_json_c.lane("3355", "3341", 118.362, 10.0),
				(Object[]) rupco_json_c.lane("3177", "2636", 210.214, 10.0),
				(Object[]) rupco_json_c.lane("1132", "1975", 11.0, 10.0),
				(Object[]) rupco_json_c.lane("1501", "3601", 104.939, 10.0),
				(Object[]) rupco_json_c.lane("3414", "3425", 18.792, 10.0),
				(Object[]) rupco_json_c.lane("3414", "1739", 55.978, 10.0),
				(Object[]) rupco_json_c.lane("3259", "1413", 23.05, 10.0),
				(Object[]) rupco_json_c.lane("3259", "1132", 150.222, 10.0),
				(Object[]) rupco_json_c.lane("2173", "3402", 125.089, 10.0),
				(Object[]) rupco_json_c.lane("3223", "3234", 18.784, 10.0),
				(Object[]) rupco_json_c.lane("3223", "3198", 125.912, 10.0),
				(Object[]) rupco_json_c.lane("3272", "3283", 20.531, 10.0),
				(Object[]) rupco_json_c.lane("3272", "3284", 93.208, 10.0),
				(Object[]) rupco_json_c.lane("149", "205", 110.415, 3.0),
				(Object[]) rupco_json_c.lane("2636", "3319", 130.111, 10.0),
				(Object[]) rupco_json_c.lane("3271", "3260", 20.302, 10.0),
				(Object[]) rupco_json_c.lane("3271", "3330", 129.449, 10.0),
				(Object[]) rupco_json_c.lane("2486", "3210", 79.398, 10.0),
				(Object[]) rupco_json_c.lane("2773", "3355", 85.916, 10.0),
				(Object[]) rupco_json_c.lane("1739", "2070", 74.061, 10.0),
				(Object[]) rupco_json_c.lane("3368", "3389", 107.119, 10.0),
				(Object[]) rupco_json_c.lane("3366", "3343", 207.476, 10.0),
				(Object[]) rupco_json_c.lane("2286", "2571", 346.451, 10.0),
				(Object[]) rupco_json_c.lane("3330", "1512", 224.441, 10.0),
				(Object[]) rupco_json_c.lane("3466", "3177", 38.714, 10.0),
				(Object[]) rupco_json_c.lane("3425", "2023", 77.777, 10.0),
				(Object[]) rupco_json_c.lane("53", "249", 17.214, 3.0),
				(Object[]) rupco_json_c.lane("53", "78", 48.898, 4.0),
				(Object[]) rupco_json_c.lane("3427", "3477", 208.471, 10.0),
				(Object[]) rupco_json_c.lane("78", "84", 11.015, 3.0),
				(Object[]) rupco_json_c.lane("2111", "3403", 123.144, 10.0) };

		Object[] vspec = new Object[] {
				(Object[]) rupco_json_c.vehicle("72", 2.4, 8.333333333333334,
						"3179", "3490", 0.0),
				(Object[]) rupco_json_c.vehicle("73", 2.4, 8.333333333333334,
						"3179", "3490", 0.0),
				(Object[]) rupco_json_c.vehicle("70", 2.4, 8.333333333333334,
						"2231", "3181", 53.0),
				(Object[]) rupco_json_c.vehicle("2", 2.4, 8.333333333333334,
						"3179", "3490", 0.0),
				(Object[]) rupco_json_c.vehicle("71", 2.4, 8.333333333333334,
						"2231", "3181", 59.0) };

		double safety_distance = 2;
		double zone_size = 5;
		double avg_borarding_decending_time = 2;

		URL url = new URL("http://localhost:8080");
		JsonRpcHttpClient client = new JsonRpcHttpClient(url);
		
		client.invoke("init_rupco", new Object[] { "IAT", nspec, lspec, vspec,
				safety_distance, zone_size, avg_borarding_decending_time },
				Object.class);
		
		client.invoke("set_Jave_en", new Object[] {}, Object.class);

		Object[][] W = new Object[][] { (Object[]) rupco_json_c.waiting_info(
				"2286",
				new String[] { "B150703161752.678", "B150703161758.805" }) };

		Object[][] V = new Object[][] {
				(Object[]) rupco_json_c.vehicle_info("72", "1975", "3236", 0.0,
						new String[] {}, 0),
				(Object[]) rupco_json_c.vehicle_info("73", "1975", "3236", 0.0,
						new String[] {}, 0),
				(Object[]) rupco_json_c.vehicle_info("70", "3179", "3490", 0.0,
						new String[] {}, 0),
				(Object[]) rupco_json_c.vehicle_info("2", "3179", "3490", 0.0,
						new String[] {}, 0),
				(Object[]) rupco_json_c.vehicle_info("71", "2286", "2571", 0.0,
						new String[] {}, 2) };

		Object p = client.invoke("redispatching", new Object[] { V, W }, Object.class);
		display_plan(p);
		p = client.invoke("route", new Object[] { "71", "2571", V}, Object.class);
		display_plan(p);
	}
	
	static void display_plan(Object p) {
		ArrayList planning = (ArrayList) p;
		for (int i =0 ; i< planning.size();i++){
			ArrayList a_plan = (ArrayList) planning.get(i);
			System.out.print(a_plan.get(0) + ": " +a_plan.get(1) + " ("+a_plan.get(2)+")");
			System.out.println();
		}
	}
}
