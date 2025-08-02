# MCP Chat Assistant

A simple chat application using MCP (Model Context Protocol) with built-in conversation memory and multiple tool integrations.

## Features

- 🤖 **AI Assistant**: Powered by Groq's Llama 3.3 70B model
- 🧠 **Conversation Memory**: Maintains context across conversations
- 🔧 **Multiple Tools**: Browser automation, web search, and Airbnb integration
- 💬 **Interactive Chat**: Real-time conversation interface
- 🛡️ **Error Handling**: Robust error handling with helpful suggestions

## Available Tools

- **Browser Automation**: Navigate, click, type, and interact with web pages
- **Web Search**: Search the web using DuckDuckGo
- **Airbnb Integration**: Search for accommodations (may be limited by robots.txt)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "Build An AI Assistant Using MCP"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### Running the Application

```bash
python app.py
```

### Available Commands

- `help` - Show available commands and tips
- `clear` - Clear conversation history
- `exit` or `quit` - End the conversation

### Example Interactions

```
😎 YOU 👉 help
📋 Available Commands:
- 'exit' or 'quit': End the conversation
- 'clear': Clear conversation history
- 'help': Show this help message

💡 Tips:
- Be specific with your requests
- For web searches, try: 'search for [topic]'
- For browser actions, try: 'open [website]'
- For travel info, try: 'find hotels in [city]'

😎 YOU 👉 search for best restaurants in New York
💭 Assistant 👉 I'll search for the best restaurants in New York for you...

😎 YOU 👉 open google.com
💭 Assistant 👉 I'll open Google's homepage for you...
```

## Recent Fixes

### Version 2.0 - Error Handling Improvements

**Issues Fixed:**
1. **Tool Validation Errors**: Fixed parameter type mismatches in tool calls
2. **Robots.txt Blocking**: Added graceful handling for blocked websites
3. **Agent Crashes**: Improved error handling to prevent application crashes
4. **User Experience**: Added helpful error messages and suggestions

**Key Improvements:**
- ✅ Custom system prompt for better tool usage
- ✅ Reduced max steps to prevent infinite loops
- ✅ Better error categorization and user guidance
- ✅ Graceful handling of tool failures
- ✅ Improved logging configuration
- ✅ Enhanced user interface with emojis and clear messaging

### Technical Details

**Error Handling:**
- Catches and categorizes different types of errors
- Provides specific suggestions based on error type
- Graceful fallback when tools are unavailable

**Tool Usage Guidelines:**
- Validates parameters before tool calls
- Uses appropriate data types (numbers for counts, strings for text)
- Handles robots.txt restrictions gracefully

**Memory Management:**
- Built-in conversation memory for context
- Ability to clear history when needed
- Proper cleanup of resources

## Troubleshooting

### Common Issues

1. **"robots.txt" errors**: Some websites block automated access
   - **Solution**: Try different approaches or be more specific in requests

2. **Tool validation errors**: Parameter type mismatches
   - **Solution**: The system now handles this automatically, but you can try rephrasing

3. **Timeout errors**: Requests taking too long
   - **Solution**: Try simpler queries or wait and retry

4. **API key issues**: Make sure your `.env` file contains the correct GROQ_API_KEY

### Getting Help

- Use the `help` command in the chat
- Check the error messages for specific guidance
- Ensure all dependencies are properly installed

## Testing

Run the test script to verify functionality:

```bash
python test_app.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to submit issues and enhancement requests!
