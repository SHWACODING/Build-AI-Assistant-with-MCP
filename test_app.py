"""
Test script for the MCP Chat Application
"""

import asyncio
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import run_memory_chat

async def test_basic_functionality():
    """Test basic functionality of the chat application"""
    print("🧪 Testing MCP Chat Application...")
    
    try:
        # This will start the chat application
        # You can test it by typing 'help' and then 'exit'
        await run_memory_chat()
        print("✅ Test completed successfully!")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 Starting MCP Chat Application Test...")
    success = asyncio.run(test_basic_functionality())
    
    if success:
        print("🎉 All tests passed!")
    else:
        print("💥 Tests failed!")
        sys.exit(1) 