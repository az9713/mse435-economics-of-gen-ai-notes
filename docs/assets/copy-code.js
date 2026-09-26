document.querySelectorAll('pre').forEach((pre) => {
  const wrapper = document.createElement('div');
  wrapper.className = 'code-wrapper';
  pre.before(wrapper);
  wrapper.append(pre);
  const button = document.createElement('button');
  button.className = 'copy-code';
  button.type = 'button';
  button.textContent = 'Copy code';
  button.setAttribute('aria-label', 'Copy code example');
  wrapper.append(button);
  button.addEventListener('click', async () => {
    const text = (pre.querySelector('code') || pre).textContent;
    try {
      if (navigator.clipboard) {
        await navigator.clipboard.writeText(text);
      } else {
        const field = document.createElement('textarea');
        field.value = text;
        wrapper.append(field);
        field.select();
        const copied = document.execCommand('copy');
        field.remove();
        if (!copied) throw new Error('Clipboard unavailable');
      }
      button.textContent = 'Copied';
    } catch {
      button.textContent = 'Select code to copy';
    }
  });
});
