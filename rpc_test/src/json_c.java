import java.net.URL;
import com.googlecode.jsonrpc4j.JsonRpcHttpClient;

public class json_c {

	public static void main(String[] args) throws Throwable {

		URL url = new URL("http://localhost:8080");
		JsonRpcHttpClient client = new JsonRpcHttpClient(url);

		Object rv = client.invoke("add", new Object[] {1, 2}, Object.class);
		System.out.println(rv);
		rv = client.invoke("echo", new Object[] {"echo test"}, Object.class);
		System.out.println(rv);
		String rv1 = client.invoke("hello", new Object[] {}, String.class);
		System.out.println(rv1);
	}
}
