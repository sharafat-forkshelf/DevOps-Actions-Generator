import streamlit as st
import os
from utils import scan_directory
from logic import identify_stack, generate_workflow

st.set_page_config(page_title="DevOps Actions Generator", page_icon="🚀", layout="wide")

st.title("CI/CA Actions Generator")
st.markdown("Scan your project and generate GitHub Actions workflows using Gemini.")

# Sidebar
with st.sidebar:
    st.header("Configuration")

    # Check for API Key
    if os.getenv("GEMINI_API_KEY"):
        st.success("GEMINI_API_KEY found!")
    else:
        st.error("GEMINI_API_KEY not found in .env")
        st.info("Please add your key to the .env file.")

    # Directory Picker
    if 'current_path' not in st.session_state:
        st.session_state.current_path = os.getcwd()

    st.write(f"**Current Path:** `{st.session_state.current_path}`")

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("⬆️"):
            st.session_state.current_path = os.path.dirname(st.session_state.current_path)
            st.rerun()

    with col2:
        try:
            subdirs = [d for d in os.listdir(st.session_state.current_path)
                      if os.path.isdir(os.path.join(st.session_state.current_path, d))
                      and not d.startswith('.')]
            subdirs.sort()
            selected_subdir = st.selectbox("Go to subdirectory", ["Select..."] + subdirs, label_visibility="collapsed")
            if selected_subdir and selected_subdir != "Select...":
                st.session_state.current_path = os.path.join(st.session_state.current_path, selected_subdir)
                st.rerun()
        except PermissionError:
            st.error("Permission denied")
        except Exception as e:
            st.error(f"Error: {e}")

    project_path = st.session_state.current_path

# Main Content
if 'project_context' not in st.session_state:
    st.session_state.project_context = None

if st.button("Scan Project"):
    with st.spinner("Scanning directory..."):
        context = scan_directory(project_path)
        if context.startswith("Error"):
            st.error(context)
        else:
            st.session_state.project_context = context
            st.success("Scan complete!")

if st.session_state.project_context:
    st.subheader("Project Analysis")

    if 'stack_analysis' not in st.session_state:
        with st.spinner("Analyzing stack with Gemini..."):
            st.session_state.stack_analysis = identify_stack(st.session_state.project_context)

    st.write(st.session_state.stack_analysis)

    st.divider()

    st.subheader("Generate Workflows")

    workflow_options = ["CI (Continuous Integration)", "Linting", "Security Audit", "Docker Build & Push", "Release"]
    selected_workflow = st.selectbox("Select Workflow Type", workflow_options)

    if st.button("Generate YAML"):
        with st.spinner(f"Generating {selected_workflow} workflow..."):
            yaml_content = generate_workflow(st.session_state.project_context, selected_workflow)
            st.code(yaml_content, language='yaml')

            # Extract YAML content from code block if present
            clean_yaml = yaml_content
            if "```yaml" in yaml_content:
                clean_yaml = yaml_content.split("```yaml")[1].split("```")[0].strip()
            elif "```" in yaml_content:
                clean_yaml = yaml_content.split("```")[1].split("```")[0].strip()

            st.download_button(
                label="Download YAML",
                data=clean_yaml,
                file_name=f"{selected_workflow.split()[0].lower()}.yml",
                mime="text/yaml"
            )
