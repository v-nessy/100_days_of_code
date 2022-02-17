function reddenPage() {
  document.body.style.backgroundColor = '#6200ff';
}

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: reddenPage
  });
});
