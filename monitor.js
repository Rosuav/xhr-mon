const XMLHttpOriginal = window.XMLHttpRequest;

class XMLHttpRequest extends XMLHttpOriginal {
	constructor() {
		super();
		this.addEventListener("readystatechange", e => {
			if (this.readyState != 4) return;
			if (this.status === 204) return; //No response
			const req = {
				ts: +new Date(),
				url: this.responseURL,
				status: this.status,
				type: this.responseType,
				headers: this.getAllResponseHeaders(),
			};
			if (this.responseType === "" || this.responseType === "text")
				req.data = this.responseText;
			else if (this.responseType === "arraybuffer")
				req.data = [...new Uint8Array(this.response)];
			else
				req.data = null;
			fetch("http://localhost:5000/save", {
				method: "POST",
				headers: {"content-type": "application/json"},
				body: JSON.stringify(req),
			});
		});
	}
}
window.XMLHttpRequest = XMLHttpRequest;
